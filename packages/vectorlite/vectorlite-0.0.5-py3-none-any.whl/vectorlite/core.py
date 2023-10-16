import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch
from hnswlib import Index

class VectorLite:
    def __init__(self):
        self.db = []
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None

    def _initialize_index(self, dim):
        self.index = Index(space='cosine', dim=dim)
        self.index.init_index(max_elements=1000000, ef_construction=200, M=16)

    def create(self, data):
        embeddings = self.embedder.encode(data)
        if not self.index:
            self._initialize_index(embeddings[0].shape[0])
        for idx, item in enumerate(data):
            self.db.append(item)
            self.index.add_items(embeddings[idx], idx)

    def read(self, idx):
        return self.db[idx]

    def update(self, idx, new_data):
        self.db[idx] = new_data
        new_embedding = self.embedder.encode(new_data)
        self.index.add_items(new_embedding, idx)

    def delete(self, idx):
        del self.db[idx]
        self.index.mark_deleted(idx)

    def similarity_search(self, query):
        query_embedding = self.embedder.encode(query)
        labels, distances = self.index.knn_query(query_embedding, k=5)
        return [self.db[idx] for idx in labels[0]]

    def semantic_search(self, query):
        query_embedding = self.embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, torch.tensor(self.embedder.encode(self.db)))
        top_results = torch.topk(cos_scores, k=5)
        return [self.db[idx] for idx in top_results.indices]
