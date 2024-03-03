from importlib.resources import path
from inspect import getfile
from sys import argv
from pathlib import Path
import os
from datetime import datetime
import urllib
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil
from fastapi import FastAPI

app = FastAPI()

c = 11
enfile = ""

fil = os.listdir('/Users/chirag/Desktop/er/')


def _chunk_file(file, ofile, extension):
    # ... existing code of _chunk_file ...


def _split():
    # ... existing code of _split ...


def _post(file, exe):
    # ... existing code of _post ...


def encry():
    # ... existing code of encry ...


def _fetch():
    # ... existing code of _fetch ...


def _join():
    # ... existing code of _join ...


def decry():
    # ... existing code of decry ...


@app.post("/split/")
def split_endpoint():
    _split()


@app.post("/join/")
def join_endpoint():
    _join()


@app.post("/encrypt/")
def encrypt_endpoint():
    encry()


@app.post("/decrypt/")
def decrypt_endpoint():
    decry()


@app.post("/fetch/")
def fetch_endpoint():
    _fetch()


def main():
    command = argv[1]

    if command.lower() == 'split':
        _split()
    elif command.lower() == 'join':
        _join()
    elif command.lower() == 'ency':
        encry()
    elif command.lower() == 'decy':
        decry()
    elif command.lower() == 'fec':
        _fetch()
    else:
        print('use either split or join')


if __name__ == '__main__':
    main()