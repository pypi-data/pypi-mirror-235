# VectorLiteDB

Lightweight vector database. VectorLite is like the SQLite of vector databases.

## 🚀 Quick Install

```pip install vectorlite```

## Usage

### Functional

```
from vectorlite import VectorLite

vl = VectorLite()
data = ["A man is eating food.", "A man is eating a piece of bread."]
vl.create(data)

# Searching
results = vl.similarity_search("A man is eating pasta.")
print(results)
```

### Run as server

1. ```serve vectorlite```

2. Navigate to http://localhost:4440/docs



