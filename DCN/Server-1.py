from fastapi import FastAPI
from pathlib import Path
import os
import time
from cryptography.fernet import Fernet
import pyrebase
import shutil

app = FastAPI()

c = 11
enfile = ""

fil = os.listdir('/Users/chirag/Desktop/er/')


@app.post("/split/")
async def split():
    p = Path.cwd()
    file_to_split = None
    for f in p.iterdir():
        if f.is_file() and f.name[0] != '.':
            file_to_split = f
            break
    oooo = os.path.basename(file_to_split)
    aexe = file_to_split.suffix
    if file_to_split:
        with open(file_to_split, 'rb') as file:
            _chunk_file(file, file_to_split, aexe)


@app.post("/chunk_file/")
async def chunk_file(file: str, ofile: str, extension: str):
    tot = 0
    start_time = time.perf_counter()
    oooo = os.path.basename(ofile)
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
    end_time = time.perf_counter()
    tot += end_time - start_time
    print("|slice--", end_time - start_time, "seconds")
    field = os.listdir('/Users/chirag/Desktop/er/')
    field.sort(reverse=True)
    counter = 0
    for i in field:
        counter = counter + 1
    a = counter
    for filw in range(0, a, 2):
        if field[filw] != ".DS_Store" and field[filw] != "encrypted" + extension:
            os.remove(field[filw])
    _post(oooo, extension)


@app.post("/post/")
async def post(file: str, exe: str):
    tot = 0
    fil1 = os.listdir('/Users/chirag/Desktop/er/')
    print(file)
    enfile = file
    for filr1 in fil1:
        if filr1 != ".DS_Store" and filr1 != file:
            filz1 = filr1
            start_time = time.perf_counter()
            firebaseConfig = {add firebase configration for your server}
            firebase = pyrebase.initialize_app(firebaseConfig)
            storage = firebase.storage()
            child_on_path = "" + filz1 + ""
            path_local = "" + filz1 + ""
            storage.child(child_on_path).put(path_local)
            end_time = time.perf_counter()
            tot += end_time - start_time
            print("" + filz1 + "|--", end_time - start_time, "seconds")
    print("TOTAL RUNTIME|--", tot, "seconds")
    for fillls in fil1:
        if fillls != file:
            os.remove("" + fillls + "")


@app.post("/encry/")
async def encry():
    tot = 0
    p = Path.cwd()
    file_to_split = None
    for f in p.iterdir():
        if f.is_file() and f.name[0] != '.':
            file_to_split = f
            break
    oooo = os.path.basename(file_to_split)
    print(oooo)
    start_time = time.perf_counter()
    s = os.path.getsize(oooo)
    print(s)
    os.chdir('/Users/chirag/Desktop/key/')
    key = Fernet.generate_key()
    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)
    f = Fernet(key)
    os.chdir('/Users/chirag/Desktop/er/')
    with open(oooo, 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open('encrypted' + file_to_split.suffix, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.chdir('/Users/chirag/Desktop/re/')
    with open('encrypted' + file_to_split.suffix, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.chdir('/Users/chirag/Desktop/er/')
    fil = os.listdir('/Users/chirag/Desktop/er/')
    for fillls in fil:
        if fillls != "encrypted" + file_to_split.suffix + "":
            os.remove("" + fillls + "")
    aexe = file_to_split.suffix
    file_to_split = "encrypted" + file_to_split.suffix + ""
    end_time = time.perf_counter()
    tot += end_time - start_time
    print("|--", end_time - start_time, "seconds")


@app.post("/fetch/")
async def fetch():
    tot = 0
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/er/')
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
        firebaseConfig = {add firebase configration for your server}
        firebase = pyrebase.initialize_app(firebaseConfig)
        storage = firebase.storage()
        storage.child(tip).download('/Users/chirag/Desktop/dwn/', tip)
        end_time = time.perf_counter()
        tot += end_time - start_time
        print("" + str(count) + "" + aka + ".chk|--", end_time - start_time, "seconds")
    print("TOTAL RUNTIME|--", tot, "seconds")


@app.post("/join/")
async def join():
    tot = 0
    start_time = time.perf_counter()
    fil = os.listdir('/Users/chirag/Desktop/er/')
    oooo = os.path.basename(fil[0])
    os.chdir('/Users/chirag/Desktop/dwn/')
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/dwn/')
    chunks = list(p.rglob('*.chk'))
    chunks.sort()
    for chunk in chunks:
        print(chunk)
    extension = chunks[0].suffixes[0]
    with open('encrypted' + extension, 'ab') as file:
        for chunk in chunks:
            with open(chunk, 'rb') as piece:
                while True:
                    bfr = piece.read(read_buffer_size)
                    if not bfr:
                        break
                    file.write(bfr)
    for fillls in fil:
        if fillls != oooo:
            os.remove("" + fillls + "")
    os.chdir('/Users/chirag/Desktop/re/')
    chunks = os.listdir('/Users/chirag/Desktop/re/')
    for chunk in chunks:
        if chunk != "encrypted" + extension + "" and chunk != ".DS_Store":
            os.remove(chunk)
    os.chdir('/Users/chirag/Desktop/er/')
    chunks = os.listdir('/Users/chirag/Desktop/er/')
    for chunk in chunks:
        if chunk != "encrypted" + extension + "" and chunk != ".DS_Store":
            os.remove(chunk)
    end_time = time.perf_counter()
    tot += end_time - start_time
    print("|--", end_time - start_time, "seconds")


@app.post("/decry/")
async def decry():
    tot = 0
    start_time = time.perf_counter()
    fil = os.listdir('/Users/chirag/Desktop/er/')
    oooo = os.path.basename(fil[0])
    os.chdir('/Users/chirag/Desktop/key/')
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()
    os.chdir('/Users/chirag/Desktop/dwn/')
    f = Fernet(key)
    with open(oooo, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open(oooo, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    end_time = time.perf_counter()
    tot += end_time - start_time
    print("|--", end_time - start_time, "seconds")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)