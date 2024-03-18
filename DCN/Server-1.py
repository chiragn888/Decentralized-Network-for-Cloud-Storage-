from fastapi import FastAPI, HTTPException
import os
from pathlib import Path
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil
from importlib.resources import path
from inspect import getfile
from sys import argv
from datetime import datetime
from turtle import clear
import urllib

app = FastAPI()

# ... rest of the existing code with changes as described in the specific changes ...

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

def main():
    # Existing logic here...
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)