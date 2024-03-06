from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from pathlib import Path
import os
import time
from cryptography.fernet import Fernet
import pyrebase

app = FastAPI()

# ... (rest of the functions remain unchanged)

@app.post("/process/")
async def process_command(command: str, file_path: Optional[str] = None):
    if command.lower() == 'split':
        return _split()
    elif command.lower() == 'join':
        return _join()
    elif command.lower() == 'ency':
        return encry()
    elif command.lower() == 'decy':
        return decry()
    elif command.lower() == 'fec':
        return _fetch()
    else:
        return {"error": "Invalid command"}

# ... (rest of the functions remain unchanged)

def _chunk_file(file, ofile, extension):
    # ... (rest of the code remains unchanged)

def _split():
    # ... (rest of the code remains unchanged)

def _post(file, exe):
    # ... (rest of the code remains unchanged)

def encry():
    # ... (rest of the code remains unchanged)

def _fetch():
    # ... (rest of the code remains unchanged)

def _join():
    # ... (rest of the code remains unchanged)

def decry():
    # ... (rest of the code remains unchanged)

def main():
    # ... (rest of the code remains unchanged)

if __name__ == '__main__':
    main()