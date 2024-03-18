from fastapi import FastAPI
from inspect import getfile
from sys import argv
from pathlib import Path
import os
from datetime import datetime
import time
from cryptography.fernet import Fernet
import pyrebase

app = FastAPI()

c = 11
enfile = ""

fil = os.listdir('/Users/chirag/Desktop/er/')


def _chunk_file(file, ofile, extension):
    # ... existing code ...


def _split():
    # ... existing code ...


def _post(file, exe):
    # ... existing code ...


def encry():
    # ... existing code ...


def _fetch():
    # ... existing code ...


def _join():
    # ... existing code ...


def decry():
    # ... existing code ...


@app.post("/split/")
def split():
    _split()
    return {"message": "Split operation completed"}


@app.post("/join/")
def join():
    _join()
    return {"message": "Join operation completed"}


@app.post("/ency/")
def ency():
    encry()
    return {"message": "Encryption operation completed"}


@app.post("/decy/")
def decy():
    decry()
    return {"message": "Decryption operation completed"}


@app.post("/fec/")
def fec():
    _fetch()
    return {"message": "Fetch operation completed"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)