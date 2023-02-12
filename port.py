import socket
import sys
from os import system

system("setterm -foreground green")
ip = input("[+]Ingrese la IP que desea escanear > ")
print("")

ip_addr = (ip)
portList = [22]

for port in portList:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))                             
        if status == 0:                     
            print(f"\033[1;31mPuerto: \033[1;32m{port} SSH - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} SSH - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        sys.exit()
