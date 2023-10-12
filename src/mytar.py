#! /usr/bin/env python3

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import string   

if len(sys.argv) < 3:
    os.write(2, "Insufficient arguments".encode())
    exit()
cmd = sys.argv[1]

if cmd == "c":
    for arg in sys.argv:
        if arg != "c" and arg != "./mytar.py":
            inputFile = os.open(arg, os.O_RDONLY)
            file_size = os.path.getsize(arg)
            byte = str(len(arg))+":"+arg+str(file_size)+":"
            byte = byte.encode()
            os.write(1, byte)
            read = os.read(inputFile, 100)
            while read != b"":
                os.write(1, read)
                read = os.read(inputFile, 100)
            os.close(inputFile)

if cmd == "x":
    inputFile = os.open(sys.argv[2], os.O_RDONLY)
    read = os.read(inputFile, 1).decode()
    while read != "":
        fNameSize = ""
        fSize = ""
        while read != ":":
            fNameSize = fNameSize + read
            read = os.read(inputFile, 1).decode()
        fName = os.read(inputFile, int(fNameSize)).decode()
        outputFile = os.open(fName, os.O_WRONLY | os.O_CREAT)
        read = os.read(inputFile, 1).decode()
        while read != ":":
            fSize = fSize + read
            read = os.read(inputFile, 1).decode()
        os.write(outputFile, os.read(inputFile, int(fSize)))
        read = os.read(inputFile, 1).decode()