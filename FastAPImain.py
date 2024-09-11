from fastapi import FastAPI, HTTPException

app = FastAPI()

items = ["one", "two"]

@app.get("/")
def root():
    return {"hello" : "world"}

@app.post("/items")
def create(item: str):
    items.append(item)
    return items

@app.get("/items")
def find_item(item_id : int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

