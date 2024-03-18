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
from fastapi import FastAPI, HTTPException

app = FastAPI()

# ... (existing functions _chunk_file, _split, _post, encry, _fetch, _join, decry remain unchanged)

@app.get("/split")
def api_split():
    _split()
    return {"message": "Split operation completed"}

@app.get("/join")
def api_join():
    _join()
    return {"message": "Join operation completed"}

@app.get("/ency")
def api_encrypt():
    encry()
    return {"message": "Encrypt operation completed"}

@app.get("/decy")
def api_decrypt():
    decry()
    return {"message": "Decrypt operation completed"}

@app.get("/fec")
def api_fetch():
    _fetch()
    return {"message": "Fetch operation completed"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)