import socket
import sys
from os import system

print("\033[1;32m ____")
print("\033[1;32m/ ___|  ___ __ _ _ __  _ __   ___ _ __")
print("\033[1;32m\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|")
print("\033[1;32m ___) | (_| (_| | | | | | | |  __/ |")
print("\033[1;32m|____/ \___\__,_|_| |_|_| |_|\___|_|")
print("\n")
system("setterm -foreground green")
ip = input("[+]Ingrese la IP que desea escanear > \033[1;37m")
print("")

ip_addr = (ip)
port1ftp = [21]
port2ssh = [22]
port3telnet = [23]
port4smb = [139]
port5netbiosns = [137]
port6microsoftds = [445]
port7dns = [53]
port8https = [443]
port9http = [80]
port10proxy = [8080]
port11pcsynchttps = [8443]
port19radanhttp  = [8088]
port20dditcp1 = [8888]
port21snmp = [161]
port22ircu = [6669]
port23trojan = [4444]
port12smtp = [25]
port13tftp = [69]
port14aed512 = [149]
port15serialgateway = [1243]
port16seagullais = [1208]
port17iasreg = [2140]
port18nmassesadmin = [3150]

print("\033[1;37m[#]Escaneando 23 puertos ...")
system("sleep 1")
print("")

for port in port1ftp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print("\033[1;33mPuerto | Servicio | Estado")
            print("")
            print(f"\033[1;31mPuerto: \033[1;32m{port} ftp - Abierto")
        else:
            print("\033[1;33mPuerto | Servicio | Estado")
            print("")
            print(f"\033[1;31mPuerto: \033[1;32m{port} ftp - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        
for port in port2ssh:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ssh - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ssh - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port3telnet:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} telnet - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} telnet - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port4smb:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} smb - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} smb - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port5netbiosns:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} netbios-ns - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} netbios-ns - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port6microsoftds:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} microsoft-ds - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} microsoft-ds - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port7dns:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} dns - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} dns - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port8https:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} https - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} https - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port9http:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} http - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} http - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port10proxy:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} proxy - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} proxy - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port11pcsynchttps:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} pcsync-https - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} pcsync-https - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port19radanhttp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} radan-http - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} radan-http - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port20dditcp1:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ddi-tcp-1 - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ddi-tcp-1 - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port21snmp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} snmp - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} snmp - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port22ircu:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ircu - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ircu - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port23trojan:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} trojan - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} trojan - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port12smtp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} smtb - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} smtb - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port13tftp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} tftp - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} tftp - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port14aed512:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} aed-512 - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} aed-512 - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port15serialgateway:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} serialgateway - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} serialgateway - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port16seagullais:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} seagull-ais - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} seagull-ais - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port17iasreg:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ias-reg - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} ias-reg - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port18nmassesadmin:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPuerto: \033[1;32m{port} nm-asses-admin - Abierto")
        else:
            print(f"\033[1;31mPuerto: \033[1;32m{port} nm-asses-admin - Cerrado")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        exit()
