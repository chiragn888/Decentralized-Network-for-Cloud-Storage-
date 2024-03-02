from fastapi import FastAPI
from dataclasses import fields
from importlib.resources import path
from inspect import getfile
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

fil = os.listdir('/Users/chirag/Desktop/re/')
for filr in fil:
 if(filr!=".DS_Store"):
  filz=os.path.getsize(r'/Users/chirag/Desktop/re/'+filr+'')

read_buffer_size = 1024
chunk_size = (15/100)*filz
print(chunk_size)

def _chunk_file(file,ofile,extension):
    # ... rest of the _chunk_file function ...

def _split():
    # ... rest of the _split function ...

def _post(file,exe):
    # ... rest of the _post function ...

def _fetch():
    # ... rest of the _fetch function ...

def _join():
    # ... rest of the _join function ...

@app.post("/split/")
async def split():
    return _split()

@app.post("/join/")
async def join():
    return _join()

@app.post("/fec/")
async def fec():
    return _fetch()

def main():
    command = argv[1]
    if command.lower() == 'split':
        _split()
    elif command.lower() == 'join':
        _join()     
    elif command.lower() == 'fec':
        _fetch()
    else:
        print('use either split or join')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)