"""
custom packet Program

Student ID: [REDECTED]
Name:       Foo Geng Hao
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script name:
    custom_packet.py

Purpose:
    creating a custom packet with spoofed source address

Usage syntax:
    to be ran through main_menu.py

Input file: (full path as on my laptop)
    nil

Output file:
    D:\school_Y1S2\PSEC\CA1-2\main_menu.py

Python Version:
    Python 3.11.0

Reference:
    nil

Library/module
    scapy - pip install scapy
    re - default libary 

Known issues:
    nil
"""
from scapy.all import send, IP, TCP
import re

def send_packets(src_addr:str , src_port:int , dest_addr:str, dest_port:int, pkt_data:str, packet_count: int):
    """sends packet with the input infomation

    Args:
        src_addr (str): source address
        src_port (int): source port 
        dest_addr (str): destination address
        dest_port (int): destination port to send to
        pkt_data (str): raw data in packet
        packet_count (int): number of packets to send
    """
    pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
    try:
        for i in range(packet_count):
            send(pkt ,verbose = False) 
        print(f'Sent {i + 1} packets')
    except:
        print('Error sending packets')

def packetInfo():
    """ask user for infomation on packet to craft

    Returns:
        str, int, str, int, str, int: source address and port, destination address and port, raw data in packet and number of packets to send
    """
    try:
        srcAddr, srcPort = addrPort('source')
        dstAddr, dstPort = addrPort('destination')
    except TypeError: # error will happen if addrPort function returns nothing
        return
    raw = input('Packet RAW Data ("DISM-DISM-DISM-DISM" if left blank): ').strip()
    if raw == '': 
        raw = "DISM-DISM-DISM-DISM" 
    try:
        count = int(input("No of Packet to send (1-65535): " ))
        if count < 1:
            print('Number has to be positive integer')
            return
        elif count > 65535:
            print('Too many packets to send')
            return
    except ValueError:
        print('Not a valid integer')
        return
    return srcAddr, srcPort, dstAddr, dstPort, raw, count

def addrPort(type: str): 
    """ask for address and port and validates both

    Args:
        type (str): whether it is asking for source or destination 

    Returns:
        str, int: returns validated address and port
    """
    addr = input(f"Enter {type} address of Packet: ").strip()
    exp = re.compile(r'^(www\.)(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)+(com)$', re.IGNORECASE)
    # [a-z0-9][a-z0-9\-]*[a-z0-9] does not allow \ or - to be the first or last character of each "block" of the url

    if not exp.fullmatch(addr): # fullmatch returns none if address is invalid
        print('Address is not valid')
        return  
    
    try:
        port = int(input(f"Enter {type} Port of Packet: "))
        if not 1 <= port <= 65535: # max port number is 65535
            print('Not a valid port')
            return
    except ValueError:
        print('Not a integer')
        return
    return addr, port

def make_packets():
    """function that uses the packetInfo function for packet infomation, and then calls function send_packets to send packets
    """
    try:
        src_addr, src_port, dest_addr, dest_port, pkt_data, packet_count = packetInfo()
    except: 
        return # if error occurs when asking for info function ends
    try:
        send_packets(src_addr, src_port, dest_addr, dest_port, pkt_data, packet_count)
    except:
        print('Packets failed to send (Maybe the addresses doesn\'t exist)')