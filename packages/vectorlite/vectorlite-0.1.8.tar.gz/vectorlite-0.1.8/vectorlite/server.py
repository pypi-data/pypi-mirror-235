from fastapi import FastAPI
from .core import VectorLite
import subprocess

app = FastAPI()
vl = VectorLite()

@app.post("/create/")
async def create(data: list[str]):
    vl.create(data)
    return {"status": "Data added successfully"}

@app.get("/read_all/")
async def read_all(max_items: int = None):
    results = vl.read_all(max_items)
    return {"results": results}

@app.get("/read/{idx}")
async def read(idx: int):
    return {"data": vl.read(idx)}

@app.put("/update/{idx}")
async def update(idx: int, new_data: str):
    vl.update(idx, new_data)
    return {"status": "Data updated successfully"}

@app.delete("/delete/{idx}")
async def delete(idx: int):
    vl.delete(idx)
    return {"status": "Data deleted successfully"}

@app.get("/similarity_search/")
async def similarity_search(query: str, k: int = 5):  # Added k as an optional query parameter with default value 5
    results = vl.similarity_search(query, k)
    return {"results": results}

@app.get("/semantic_search/")
async def semantic_search(query: str, k: int = 5):  # Added k as an optional query parameter with default value 5
    results = vl.semantic_search(query, k)
    return {"results": results}

def main():
    cmd = ["uvicorn", "vectorlite.server:app", "--host", "0.0.0.0", "--port", "4440", "--reload"]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()