""" FastAPI Web Server """
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx
from app.api.products.router import router as products_router

app = FastAPI()

# Mount the static files directory
app.mount("/statics", StaticFiles(directory="app/statics"), name="statics")

templates = Jinja2Templates(directory="app/statics/templates")

@app.get("/")
async def index(request: Request):
    """ Route for serving index.html at the root path """
    async with httpx.AsyncClient() as client:
        items = await client.get("http://localhost:8000/products/")
        items = items.json()
        return templates.TemplateResponse("index.html", {"request": request, "items": items})

app.include_router(products_router, prefix="/products", tags=["products"])
