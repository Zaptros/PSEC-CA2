"""
Main Program

Student ID: [REDECTED]
Name:       Foo Geng Hao
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script name:
    main_menu.py

Purpose:
    to run the nmap scanner, ftp client script and custom packet maker

Usage syntax:
    Run with play button in the submission folder (the folder which all the scripts and subfolders are stored)

Input file: (full path as on my laptop)
    nil
    
Output file:
    nil

Python Version:
    Python 3.11.0

Reference:
    nil
    
Library/module: 
    nil (refer to each imported script)

Known issues:
    nil
"""
# custom python functions
from ftp_client import ftpClient
from nmap_scanner import scanNetwork
from custom_packet import make_packets

# main menu
while True:
    print('\n** PSEC Info Security Apps **', '1)  Scan Network', '2)  Upload/download file using FTP', '3)  Send custom packet', '4)  Quit', sep='\n')
    try:
        userOption = int(input('>> '))
        match userOption:
            case 1:
                scanNetwork()
            case 2:
                try: # will cause error if connection cannot be made
                    ftpClient()
                except: 
                    print('Connection could not be established')
            case 3:
                make_packets()
            case 4:
                print("Bye!")
                break
            case _:
                print('Number is not one of the options')
    except ValueError:
        print('Please enter a integer')
    