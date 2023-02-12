import socket
import sys
from os import system

system("setterm -foreground green")
ip = input("[+]Ingrese la IP que desea escanear > \033[1;37m")
print("")

ip_addr = (ip)
portList = [21,22,23,139,137,445,53,443,80,8080,8443,25,69,149,1243,1208,2140,3150]

for port in portList:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        sys.exit()
