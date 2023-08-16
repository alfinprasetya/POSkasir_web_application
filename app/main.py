""" FastAPI Web Server """
import os
from fastapi import FastAPI
from fastapi.params import Body
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from nanoid import generate

items: list = [
    {"id": "item-00001", "name": "kopi", "quantity": 5000, "metric": "gram"},
    {"id": "item-00002", "name": "gula", "quantity": 2000, "metric": "gram"},
]

app = FastAPI()

# Mount the static files directory
app.mount("/statics", StaticFiles(directory="app/statics"), name="static")

@app.get("/")
async def get_index():
    """ Route for serving index.html at the root path """
    index_path = os.path.join("app/statics", "index.html")
    return FileResponse(index_path)

@app.post("/items")
async def post_item(payload: dict = Body):
    """Create New Item"""
    item_id = f'item-{generate("1234567890",5)}'
    new_item: dict = { "id": item_id, **payload }
    return new_item

@app.get("/items")
async def get_items():
    """Get All Items"""
    return items
