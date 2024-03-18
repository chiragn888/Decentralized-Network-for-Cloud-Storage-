from dataclasses import fields
from importlib.resources import path
from inspect import getfile
from sys import argv
from pathlib import Path
import os
from datetime import datetime
import urllib
import time
import pyrebase
import shutil
from fastapi import FastAPI
import uvicorn
from cryptography.fernet import Fernet

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

@app.post("/fetch")
async def fetch_files():
    _fetch()
    return {"message": "File fetching initiated."}

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Rest of the existing functions like _split, _join, _fetch, etc.

def _chunk_file(file, ofile, extension):
    # Existing code for chunking the file...

def _split():
    # Existing code for splitting the file...

def _post(file, exe):
    # Existing code for posting the file...

def _fetch():
    # Existing code for fetching the file...

def _join():
    # Existing code for joining the file...

if __name__ == '__main__':
    main()