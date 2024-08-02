"""
ftp client Program

Student ID: [REDECTED]
Name:       Foo Geng Hao
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script name:
    ftp_client.py

Purpose:
    act as client to connect to ftp_server.py

Usage syntax:
    to be ran through main_menu.py

Input file: (full path as on my laptop)
    D:\school_Y1S2\PSEC\CA1-2\ftpClientData\

Output file:
    D:\school_Y1S2\PSEC\CA1-2\ftpClientData\

Python Version:
    Python 3.11.0

Reference:
    a) how to print files in a given folder
        https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    b) ftplib package documentation
        https://docs.python.org/3/library/ftplib.html

Library/module
    os - default libary
    ftplib - default libary

Known issues:
    nil
"""
import ftplib
import os
from os.path import isfile, join # for file identifing things

clientFolder = 'ftpClientData\\'

def ftpClient():
    """ftp client that connects to the server script
    """
    ftp = ftplib.FTP()
    ftp.connect('localhost', 2121)
    ftp.login()
    print(ftp.getwelcome()) # welcome message at server

    print('Enter [1] to download file or [2] to upload file')
    userOption2 = input('>> ').strip()
    if userOption2 == '1': 
        # listing down files that can be downloaded
        fileList = ftp.nlst() # get files from server folder
        print('Files in server:')
        for f in fileList:
            print('\t'+f)

        # selecting and downloading file
        filename = input('Enter name of file to download: ').strip()
        try: # error if file is not downloaded successfully
            with open(clientFolder + filename, 'wb') as fn:
                ftp.retrbinary("RETR " + filename ,fn.write)
            print('Downloaded file: ', filename)
        except:
            print('Error in downloading: ', filename)
            os.remove(clientFolder + filename) # delete empty file that is created before error happens
        
    elif userOption2 == '2':
        # printing files at client folder
        filesandD = os.listdir(clientFolder)
        fileList = [f for f in filesandD if isfile(join(clientFolder, f))]
        print('Files in client folder:')
        for f in fileList:
            print('\t'+f)

        # selecting and uploading file
        filename = input('Enter name of file to upload: ').strip()
        try:
            ftp.storbinary('STOR ' + filename, open(clientFolder + filename, 'rb'))
            print('Uploaded file: ', filename)
        except:
            print('Error in uploading: ', filename)
    else:
        print('Invalid Option')
