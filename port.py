import socket
import sys
from os import system


print("\033[1;32m ____            _     ____  ____")
print("\033[1;32m|  _ \ ___  _ __| |_  |___ \|___ \ ")
print("\033[1;32m| |_) / _ \| '__| __|   __) | __) |")
print("\033[1;32m|  __/ (_) | |  | |_   / __/ / __/")
print("\033[1;32m|_|   \___/|_|   \__| |_____|_____|")
print("\n")
system("setterm -foreground green")
ip = input("[+]Ingrese la IP que desea escanear > \033[1;37m")
print("")

ip_addr = (ip)
portList = [22]

for port in portList:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))                             
        if status == 0:
            print("\033[1;33mPuerto | Servicio | Estado")
            print("")                     
            print(f"\033[1;31mPuerto: \033[1;32m{port} SSH - Abierto")
        else:
            print("\033[1;33mPuerto | Servicio | Estado")
            print("")
            print(f"\033[1;31mPuerto: \033[1;32m{port} SSH - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        sys.exit()

