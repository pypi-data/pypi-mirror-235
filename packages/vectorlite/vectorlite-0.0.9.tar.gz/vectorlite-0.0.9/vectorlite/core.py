import numpy as np
from sentence_transformers import SentenceTransformer, util
import torch
from hnswlib import Index

class VectorLite:
    def __init__(self):
        self.db = []
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None

    def _initialize_index(self, data_size):
        if data_size < 1000:
            ef_construction, M = 100, 8
        elif data_size < 10000:
            ef_construction, M = 200, 16
        else:
            ef_construction, M = 400, 32
        
        dim = self.embedder.get_sentence_embedding_dimension()
        self.index = Index(space='cosine', dim=dim)
        self.index.init_index(max_elements=1000000, ef_construction=ef_construction, M=M)

    def create(self, data):
        embeddings = self.embedder.encode(data)
        if not self.index:
            self._initialize_index(len(data))
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
        k_val = min(5, len(self.db))  # Adjust k based on dataset size
        labels, distances = self.index.knn_query(query_embedding, k=k_val)
        return [self.db[idx] for idx in labels[0]]

    def semantic_search(self, query):
        query_embedding = self.embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, torch.tensor(self.embedder.encode(self.db)))
        k_val = min(5, len(self.db))  # Adjust k based on dataset size
        top_results = torch.topk(cos_scores, k=k_val)
        return [self.db[idx] for idx in top_results.indices]
