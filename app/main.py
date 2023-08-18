""" FastAPI Web Server """
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
async def get_index():
    """ Route for serving index.html at the root path """
    index_path = os.path.join("app/statics", "index.html")
    return FileResponse(index_path)

# Mount the static files directory
app.mount("/", StaticFiles(directory="app/statics"), name="static")
