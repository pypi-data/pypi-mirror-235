from fastapi import FastAPI
from vectorlite import VectorLite
import subprocess

app = FastAPI()
vl = VectorLite()

@app.post("/create/")
async def create(data: list[str]):
    vl.create(data)
    return {"status": "Data added successfully"}

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
async def similarity_search(query: str):
    return {"results": vl.similarity_search(query)}

@app.get("/semantic_search/")
async def semantic_search(query: str):
    return {"results": vl.semantic_search(query)}

def main():
    cmd = ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "4440", "--reload"]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()