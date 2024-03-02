from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import os
from pathlib import Path
import time
import shutil
import pyrebase

app = FastAPI()

def _chunk_file(file, ofile, extension, chunk_size):
    # Code for chunking the file
    # ...

def _split(file, chunk_size_percent):
    # Code for splitting the file
    # ...

def _post(file, exe, firebase_config):
    # Code for posting the file to Firebase
    # ...

def _fetch(file_name, firebase_config):
    # Code for fetching file from Firebase
    # ...

def _join(chunks):
    # Code for joining the file chunks
    # ...

@app.post("/split/")
async def split(file: UploadFile = File(...), chunk_size_percent: float = 15.0):
    # Call the _split function with the file and chunk size percent
    _split(file, chunk_size_percent)

@app.post("/join/")
async def join(chunks: List[UploadFile] = File(...)):
    # Call the _join function with the file chunks
    _join(chunks)

@app.post("/fetch/")
async def fetch(file_name: str, firebase_config: dict):
    # Call the _fetch function with the file name and Firebase configuration
    _fetch(file_name, firebase_config)