from fastapi import FastAPI
from importlib.resources import path
from inspect import getfile
from sys import argv
from pathlib import Path
import os
from datetime import datetime
from turtle import clear
import urllib
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil
import uvicorn

app = FastAPI()

c = 11
enfile = ""

fil = os.listdir('/Users/chirag/Desktop/er/')

# ... rest of the unchanged code ...

@app.post("/split/")
async def split():
    return _split()

@app.post("/join/")
async def join():
    return _join()

@app.post("/ency/")
async def ency():
    return encry()

@app.post("/decy/")
async def decy():
    return decry()

@app.post("/fec/")
async def fec():
    return _fetch()

# ... rest of the unchanged code ...

def _chunk_file(file, ofile, extension):
    # ... rest of the original _chunk_file function ...

def _split():
    # ... rest of the original _split function ...

def _post(file, exe):
    # ... rest of the original _post function ...

def encry():
    # ... rest of the original encry function ...

def _fetch():
    # ... rest of the original _fetch function ...

def _join():
    # ... rest of the original _join function ...

def decry():
    # ... rest of the original decry function ...

def main():
    # ... rest of the original main function ...

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)