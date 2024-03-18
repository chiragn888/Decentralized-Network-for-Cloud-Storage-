from pathlib import Path
import os
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil
from fastapi import FastAPI, HTTPException

app = FastAPI()

read_buffer_size = 1024
chunk_size = (15/100)*filz

# ... (existing functions _chunk_file, _split, _post, _fetch, _join remain unchanged)

@app.get("/split")
def api_split():
    _split()
    return {"message": "Split operation completed"}

@app.get("/join")
def api_join():
    _join()
    return {"message": "Join operation completed"}

@app.get("/fetch")
def api_fetch():
    _fetch()
    return {"message": "Fetch operation completed"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def _chunk_file(file, ofile, extension):
    # Existing logic from original code
    pass

def _split():
    # Existing logic from original code
    pass

def _post(file, exe):
    # Existing logic from original code
    pass

def _fetch():
    # Existing logic from original code
    pass

def _join():
    # Existing logic from original code
    pass

def main():
    # Existing logic from original code
    pass