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

c=11
enfile=""

fil = os.listdir('/Users/chirag/Desktop/er/')


for filr in fil:
   if(filr!=".DS_Store"):
       filz=os.path.getsize(r'/Users/chirag/Desktop/er/'+filr+'')

read_buffer_size = 1024
chunk_size = (15/100)*filz
print(chunk_size)




def _chunk_file(file,ofile,extension):
     
        tot=0
        start_time = time.perf_counter ()
        oooo=os.path.basename(ofile)
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
        end_time = time.perf_counter ()
        tot+=end_time - start_time
        print("|slice--",end_time - start_time, "seconds")

        field = os.listdir('/Users/chirag/Desktop/er/')    
        field.sort(reverse=True)  
        counter = 0
        for i in field:     
            counter = counter + 1
        a=counter
        for filw in range(0,a,2):
            if(field[filw]!=".DS_Store" and field[filw]!="encrypted"+extension):
              os.remove(field[filw])
                        
        _post(oooo,extension)                      
        

def _split():

    p = Path.cwd()

    file_to_split = None
    for f in p.iterdir():
        if f.is_file() and f.name[0] != '.':
            file_to_split = f
            break
    oooo=os.path.basename(file_to_split)
    aexe=file_to_split.suffix    

               
    if file_to_split:
        with open(file_to_split, 'rb') as file: 
            _chunk_file(file,file_to_split,aexe)
            



def _post(file,exe):
        
        tot=0
        fil1 = os.listdir('/Users/chirag/Desktop/er/')
        print(file)
        enfile=file
        for filr1 in fil1:
         if(filr1!=".DS_Store" and filr1!=file):
            filz1=filr1

            start_time = time.perf_counter ()
            firebaseConfig={"apiKey": "AIzaSyCnX3WSF17-fcIyIO8lFSweZZXGOAAmxvo",
                    "authDomain": "ipvp-777b1.firebaseapp.com",
                    "databaseURL": "https://ipvp-777b1-default-rtdb.firebaseio.com",
                    "projectId": "ipvp-777b1",
                    "storageBucket": "ipvp-777b1.appspot.com",
                    "messagingSenderId": "26128863320",
                    "appId": "1:26128863320:web:a64d5e23e27ae68104ba2d",
                    "measurementId": "G-QB4JQ6J4CZ"}

            firebase=pyrebase.initialize_app(firebaseConfig)
            storage=firebase.storage()
            child_on_path=""+filz1+""
            path_local= ""+filz1+""
            storage.child(child_on_path).put(path_local)
            
            end_time = time.perf_counter ()
            tot+=end_time - start_time
            print(""+filz1+"|--",end_time - start_time, "seconds")
            
        print("TOTAL RUNTIME|--",tot,"seconds")      
        for fillls in fil1:
                if(fillls!=file):
                    os.remove(""+fillls+"")      




def encry():
    tot=0
    p = Path.cwd()

    file_to_split = None
    for f in p.iterdir():
        if f.is_file() and f.name[0] != '.':
            file_to_split = f
            break

    oooo=os.path.basename(file_to_split)
    print(oooo)
    start_time = time.perf_counter ()
    s=os.path.getsize(oooo)
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

    with open ('encrypted'+file_to_split.suffix, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    os.chdir('/Users/chirag/Desktop/re/')
    with open ('encrypted'+file_to_split.suffix, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    os.chdir('/Users/chirag/Desktop/er/')        

    fil = os.listdir('/Users/chirag/Desktop/er/')


    for fillls in fil:
                if(fillls!="encrypted"+file_to_split.suffix+""):
                    os.remove(""+fillls+"") 
    aexe=file_to_split.suffix
    file_to_split="encrypted"+file_to_split.suffix+""
    end_time = time.perf_counter ()
    tot+=end_time - start_time
    print("|--",end_time - start_time, "seconds")



def _fetch():

    tot=0
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/er/')
    for files in fil:
        if(files!=".DS_Store"):
                split_tup = os.path.splitext(files)
                aka=split_tup[1]
                print(aka)

    os.chdir('/Users/chirag/Desktop/dwn/')
    for count in range(0,11):
        count+=1
        tip = ""+str(count)+""+aka+".chk"
        start_time = time.perf_counter ()
        firebaseConfig={"apiKey": "AIzaSyCnX3WSF17-fcIyIO8lFSweZZXGOAAmxvo",
                        "authDomain": "ipvp-777b1.firebaseapp.com",
                        "databaseURL": "https://ipvp-777b1-default-rtdb.firebaseio.com",
                        "projectId": "ipvp-777b1",
                        "storageBucket": "ipvp-777b1.appspot.com",
                        "messagingSenderId": "26128863320",
                        "appId": "1:26128863320:web:a64d5e23e27ae68104ba2d",
                        "measurementId": "G-QB4JQ6J4CZ"}

        firebase=pyrebase.initialize_app(firebaseConfig)
        storage=firebase.storage()

        storage.child(tip).download('/Users/chirag/Desktop/dwn/',tip)
        end_time = time.perf_counter ()
        tot+=end_time - start_time
        print(""+str(count)+""+aka+".chk|--",end_time - start_time, "seconds")
            
    print("TOTAL RUNTIME|--",tot,"seconds")   
   

                    


def _join():
    tot=0
    start_time = time.perf_counter ()
    fil = os.listdir('/Users/chirag/Desktop/er/')
    oooo=os.path.basename(fil[0])

    os.chdir('/Users/chirag/Desktop/dwn/')
    p = Path.cwd()
    fil = os.listdir('/Users/chirag/Desktop/dwn/')
    chunks = list(p.rglob('*.chk'))
    chunks.sort()

    for chunk in chunks:
        print(chunk)

    extension = chunks[0].suffixes[0]
    with open(f'encrypted{extension}', 'ab') as file:
        for chunk in chunks:   
            with open(chunk, 'rb') as piece:
                while True:
                    bfr = piece.read(read_buffer_size)
                    if not bfr:
                        break
                    file.write(bfr)
    for fillls in fil:
                if(fillls!=oooo):
                    os.remove(""+fillls+"")  
    os.chdir('/Users/chirag/Desktop/re/')    
    chunks = os.listdir('/Users/chirag/Desktop/re/')
    for chunk in chunks:
      if(chunk!="encrypted"+extension+"" and chunk!=".DS_Store"):
         os.remove(chunk)                
    os.chdir('/Users/chirag/Desktop/er/')  
    chunks = os.listdir('/Users/chirag/Desktop/er/')
    for chunk in chunks:
      if(chunk!="encrypted"+extension+"" and chunk!=".DS_Store"):
         os.remove(chunk)   
                   
    end_time = time.perf_counter ()
    tot+=end_time - start_time
    print("|--",end_time - start_time, "seconds")

   
        

    """os.chdir('/Users/chirag/Desktop/key/')     
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    
    os.chdir('/Users/chirag/Desktop/dwn/')
    f= Fernet(key)
    with open(oooo, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(oooo, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)                                    
                
    for fillls in fil:
                if(fillls!=oooo):
                    os.remove(""+fillls+"")    """            
    

def decry():
    tot=0
    start_time = time.perf_counter ()
    fil = os.listdir('/Users/chirag/Desktop/er/')
    oooo=os.path.basename(fil[0])

    os.chdir('/Users/chirag/Desktop/key/')     
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    
    os.chdir('/Users/chirag/Desktop/dwn/')
    f= Fernet(key)
    with open(oooo, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open(oooo, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)       
    end_time = time.perf_counter ()
    tot+=end_time - start_time
    print("|--",end_time - start_time, "seconds")

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
    
