from dataclasses import fields
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
from fastapi import FastAPI

app = FastAPI()

fil = os.listdir('/Users/chirag/Desktop/re/')
for filr in fil:
 if(filr!=".DS_Store"):
  filz=os.path.getsize(r'/Users/chirag/Desktop/re/'+filr+'')

read_buffer_size = 1024
chunk_size = (15/100)*filz
print(chunk_size)

firebaseConfig = {
  'apiKey': "API_KEY",
  'authDomain': "PROJECT_ID.firebaseapp.com",
  'databaseURL': "https://PROJECT_ID.firebaseio.com",
  'storageBucket': "PROJECT_ID.appspot.com",
}

@app.post("/chunk_file/")
async def chunk_file(file: str, ofile: str, extension: str):
    # ... contents of _chunk_file function ...

@app.post("/split/")
async def split():
    # ... contents of _split function ...

@app.post("/post/")
async def post(file: str, exe: str):
    # ... contents of _post function ...

@app.post("/fetch/")
async def fetch():
    # ... contents of _fetch function ...

@app.post("/join/")
async def join():
    # ... contents of _join function ...

def _chunk_file(file, ofile, extension):
    # ... contents of _chunk_file function ...

def _split():
    # ... contents of _split function ...

def _post(file, exe):
    # ... contents of _post function ...

def _fetch():
    # ... contents of _fetch function ...

def _join():
    # ... contents of _join function ...

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
    main()