from importlib.resources import path
from inspect import getfile
from sys import argv
from pathlib import Path
import os
from datetime import datetime
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Existing code for file operations...

@app.post("/split")
async def split_files():
    _split()
    return {"message": "File splitting initiated."}

@app.post("/join")
async def join_files():
    _join()
    return {"message": "File joining initiated."}

@app.post("/encrypt")
async def encrypt_files():
    encry()
    return {"message": "File encryption initiated."}

@app.post("/decrypt")
async def decrypt_files():
    decry()
    return {"message": "File decryption initiated."}

@app.post("/fetch")
async def fetch_files():
    _fetch()
    return {"message": "File fetching initiated."}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Rest of the existing functions like _split, _join, encry, decry, _fetch, etc.

def _chunk_file(file, ofile, extension):
    # Existing logic here...
    pass

def _split():
    # Existing logic here...
    pass

def _post(file, exe):
    # Existing logic here...
    pass

def encry():
    # Existing logic here...
    pass

def _fetch():
    # Existing logic here...
    pass

def _join():
    # Existing logic here...
    pass

def decry():
    # Existing logic here...
    pass

if __name__ == '__main__':
    main()