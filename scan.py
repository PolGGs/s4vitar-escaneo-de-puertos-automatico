#!/usr/bin/env python3

import subprocess
import shlex
import re

def run_command(command):
    """Ejecuta un comando en la terminal y devuelve la salida."""
    print(f"[*] Ejecutando: {command}")
    process = subprocess.run(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
        return None
    return process.stdout

def ping_ip(ip):
    """Realiza un ping a la IP y devuelve True si responde."""
    print(f"\n[*] Haciendo ping a {ip}...")
    command = f"ping -c 1 {ip}"
    result = run_command(command)

    if result and "1 received" in result:
        print("[+] Ping exitoso: La IP está activa.")
        return True
    else:
        print("[-] Ping fallido: No se recibió respuesta.")
        return False

def scan_all_ports(ip):
    """Escanea todos los puertos abiertos y guarda el resultado en 'allPorts'."""
    print(f"\n[*] Escaneando todos los puertos en {ip} con Nmap...")
    command = f"nmap -p- --open --min-rate 5000 -vvv -n -Pn {ip} -oG allPorts"
    run_command(command)
    print("[*] Escaneo completado. Resultados guardados en 'allPorts'.")

def extract_open_ports():
    """Extrae los puertos abiertos desde el archivo allPorts y los copia al portapapeles."""
    try:
        with open("allPorts", "r") as f:
            content = f.read()
        ports = re.findall(r'(\d{1,5})/open', content)
        if ports:
            open_ports = ",".join(ports)
            # Copiar los puertos abiertos al portapapeles
            subprocess.run(shlex.split(f"echo {open_ports} | wl-copy"))
            print(f"[+] Puertos abiertos copiados al portapapeles: {open_ports}")
            return open_ports
        else:
            print("[-] No se encontraron puertos abiertos.")
            return None
    except Exception as e:
        print(f"Error al extraer puertos: {e}")
        return None

def detailed_scan(ip):
    """Realiza un escaneo detallado con scripts y detección de versiones en los puertos 22 y 80."""
    print(f"\n[*] Escaneo detallado de los puertos 22 y 80 en {ip}...")
    command = f"nmap -sC -sV --version-all -p22,80 {ip} -oN targeted"
    run_command(command)
    print("[*] Escaneo detallado completado. Resultados guardados en 'targeted'.")

if __name__ == "__main__":
    ip = input("Introduce la IP a escanear: ").strip()
    
    if ping_ip(ip):  
        scan_all_ports(ip)
        open_ports = extract_open_ports()
        
        if open_ports:
            print(f"\n[+] Puertos abiertos detectados: {open_ports}")
        else:
            print("\n[!] No se encontraron puertos abiertos.")
        
        detailed_scan(ip)
