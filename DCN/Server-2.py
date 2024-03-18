from fastapi import FastAPI, HTTPException
import os
from pathlib import Path
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil

app = FastAPI()

read_buffer_size = 1024

def _chunk_file(file, ofile, extension, chunk_size):
    current_chunk_size = 0
    current_chunk = 1
    done_reading = False
    while not done_reading:
        with open(f'{current_chunk}{extension}.chk', 'ab') as chunk:
            while True:
                bfr = file.read(read_buffer_size)
                if not bfr:
                    done_reading = True
                    break
                chunk.write(bfr)
                current_chunk_size += len(bfr)
                if current_chunk_size + read_buffer_size > chunk_size:
                    current_chunk += 1
                    current_chunk_size = 0
                    break

def _split():
    p = Path.cwd()
    file_to_split = None
    for f in p.iterdir():
        if f.is_file() and f.name[0] != '.':
            file_to_split = f
            break
    if file_to_split:
        with open(file_to_split, 'rb') as file:
            chunk_size = (15/100) * os.path.getsize(file_to_split)
            _chunk_file(file, file_to_split, file_to_split.suffix, chunk_size)

def _post(file, exe):
    tot = 0
    fil1 = os.listdir('/Users/chirag/Desktop/re/')
    for filr1 in fil1:
        if filr1 != ".DS_Store" and filr1 != "encrypted" + exe:
            filz1 = filr1
            start_time = time.perf_counter()
            firebaseConfig = {   # add firebase configuration for your server   }
            firebase = pyrebase.initialize_app(firebaseConfig)
            storage = firebase.storage()
            child_on_path = "" + filz1 + ""
            path_local = "" + filz1 + ""
            storage.child(child_on_path).put(path_local)
            end_time = time.perf_counter()
            tot += end_time - start_time
            print("" + filz1 + "|--", end_time - start_time, "seconds")
    print("TOTAL RUNTIME|--", tot, "seconds")
    fil2 = os.listdir('/Users/chirag/Desktop/re/')
    for fillls in fil2:
        if fillls != ".DS_Store" and fillls != "encrypted" + exe:
            os.remove("" + fillls + "")

def _fetch():
    tot = 0
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/re/')
    for files in fil:
        if files != ".DS_Store":
            split_tup = os.path.splitext(files)
            aka = split_tup[1]
            print(aka)
    os.chdir('/Users/chirag/Desktop/dwn/')
    for count in range(0, 11):
        count += 1
        tip = "" + str(count) + "" + aka + ".chk"
        start_time = time.perf_counter()
        firebaseConfig = {   # add firebase configuration for your server   }
        firebase = pyrebase.initialize_app(firebaseConfig)
        storage = firebase.storage()
        storage.child(tip).download('/Users/chirag/Desktop/dwn/', tip)
        end_time = time.perf_counter()
        tot += end_time - start_time
        print("" + str(count) + "" + aka + ".chk |--", end_time - start_time, "seconds")
    print("TOTAL RUNTIME|--", tot, "seconds")

def _join():
    fil = os.listdir('/Users/chirag/Desktop/re/')
    oooo = os.path.basename(fil[0])
    os.chdir('/Users/chirag/Desktop/dwn/')
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/dwn/')
    chunks = list(p.rglob('*.chk'))
    chunks.sort()
    for chunk in chunks:
        print(chunk)
    extension = chunks[0].suffixes[0]
    with open(f'join{extension}', 'ab') as file:
        for chunk in chunks:
            with open(chunk, 'rb') as piece:
                while True:
                    bfr = piece.read(read_buffer_size)
                    if not bfr:
                        break
                    file.write(bfr)
    for fillls in fil:
        if fillls != "join.png":
            os.remove("" + fillls + "")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)