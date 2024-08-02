"""
FTP Server Program

Student ID: [REDECTED]
Name:       Foo Geng Hao
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script name:
    ftp_server.py

Purpose:
    To act as the server to upload and download files

Usage syntax:
    Run with play button in the submission folder (the folder which all the scripts and subfolders are stored)

Input file: (full path as on my laptop)
    D:\school_Y1S2\PSEC\CA1-2\ftpServerData\

Output file:
    D:\school_Y1S2\PSEC\CA1-2\ftpServerData\

Python Version:
    Python 3.11.0

Reference:
    a) pyftpdlib documentation
        https://pyftpdlib.readthedocs.io/en/latest/api.html

Library/module
    pyftpdlib  -  pip install pyftpdlib

Known issues:
    nil
"""
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Instantiate a dummy authorizer for managing 'virtual' users
authorizer = DummyAuthorizer() # handle permission and user
FTPHandler.banner = "Welcome to CA1-2 FTP server" # change default banner

# Define an anonymous user and home directory having read permissions
authorizer.add_anonymous('./ftpServerData/' , perm='lrw') 
# perms: l - list files     r - reterive (download) files from server   w - store (upload) files to server

# Instantiate FTP handler class
handler = FTPHandler #  understand FTP protocol
handler.authorizer = authorizer

# Instantiate FTP server class and listen on 127.0.0.1:2121
address = ('127.0.0.1', 2121)
server = FTPServer(address, handler)

# start ftp server
server.serve_forever()