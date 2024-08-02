"""
nmap scanning Program

Student ID: [REDECTED]
Name:       Foo Geng Hao
Class:      DISM/FT/1B/01
Assessment: CA1-2

Script name:
    nmap_scanner.py

Purpose:
    use nmap to scan top 10 ports on each of the two hosts specified

Usage syntax:
    to be ran through main_menu.py

Input file: (full path as on my laptop)
    nil

Output file:
    nil
    
Python Version:
    Python 3.11.0

Reference:
    a) tabulate package documentation
        https://pypi.org/project/tabulate/
    b) nmap options
        https://nmap.org/book/man-briefoptions.html
    c) top ports option
        https://danielmiessler.com/blog/nmap-use-the-top-ports-option-for-both-tcp-and-udp-simultaneously/

Library/module
    nmap - pip install nmap (and have nmap on device)
    tabulate - pip install tabulate

Known issues:
    table of nmap scan results may be messed up if terminal size is too small - increase terminal size as much as possible to try
"""
import nmap
import tabulate

def scanNetwork():
    """function that initinates nmap scan
    """
    nmScan = nmap.PortScanner()
    print('Type of nmScan: ', type(nmScan))
    hostToScan = 'localhost scanme.nmap.org'
    print(f'Target IP     : {hostToScan}')

    options = '-sTU -T5 -O -sV -sC --traceroute --top-ports 5'  
    # -sTU - scans tcp and udp      -T5 - very aggressive nmap scanning      -O - OS detection       -sV - version detect    -sC - script scan --traceroute - traceroute    --top-ports X - scan top X ports of each protocol
    results = nmScan.scan(hosts=hostToScan, arguments=options)
    print('Type of result: ', type(results))

    table = [ ['Host','Hostname','Protocol','Port ID','State','Product','Extra info','Reason','CPE'] ] # table header
    for hostIP in results['scan']:
        hostname = results['scan'][hostIP]['hostnames'][0]['name'] # hostname from results dict
        for protocol in ['tcp','udp']: # the protocols that were scanned
            for port,v in results['scan'][hostIP][protocol].items(): # getting dictionary of each port scan out 
                tmp = [hostIP, hostname, protocol, port, v['state'], v['product'], v['extrainfo'], v['reason'], v['cpe']]
                table.append(tmp)

    print(tabulate.tabulate(table, tablefmt='simple_grid'))
    print('Time to scan: ', results['nmap']['scanstats']['elapsed'])