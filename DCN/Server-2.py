from fastapi import FastAPI
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

app = FastAPI()

fil = os.listdir('/Users/chirag/Desktop/re/')
for filr in fil:
 if(filr!=".DS_Store"):
  filz=os.path.getsize(r'/Users/chirag/Desktop/re/'+filr+'')

read_buffer_size = 1024
chunk_size = (15/100)*filz
print(chunk_size)


def _chunk_file(file, ofile, extension):
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

    field = os.listdir('/Users/chirag/Desktop/re/')
    field.sort(reverse=True)
    counter = 0
    for i in field:
        counter = counter + 1
    a = counter
    for filw in range(1, a, 2):
        if(field[filw] != ".DS_Store" and field[filw] != "encrypted" + extension):
            os.remove(field[filw])

    _post(oooo, extension)


def _split():
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


def _post(file, exe):
    tot = 0
    fil1 = os.listdir('/Users/chirag/Desktop/re/')
    print(file)
    for filr1 in fil1:
        if(filr1 != ".DS_Store" and filr1 != "encrypted" + exe):
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
    fil2 = os.listdir('/Users/chirag/Desktop/re/')
    for fillls in fil2:

        if(fillls != ".DS_Store" and fillls != "encrypted" + exe):
            os.remove("" + fillls + "")


def _fetch():
    tot = 0
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/re/')
    for files in fil:
        if(files != ".DS_Store"):
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
        if(fillls != "join.png"):
            os.remove("" + fillls + "")


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