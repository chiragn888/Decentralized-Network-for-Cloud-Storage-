from fastapi import FastAPI, HTTPException
import uvicorn
from dataclasses import fields
from pathlib import Path
import os
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil

app = FastAPI()

# Existing code for _chunk_file, _split, _post, _fetch, and _join functions comes here...

@app.get("/")
async def root():
    return {"message": "Server is running"}

@app.post("/split")
async def api_split():
    try:
        _split()
        return {"message": "File split successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/join")
async def api_join():
    try:
        _join()
        return {"message": "Files joined successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/fetch")
async def api_fetch():
    try:
        _fetch()
        return {"message": "Files fetched successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)