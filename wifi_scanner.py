import os

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def scan_wifi():
    print(f"{YELLOW}[INFO]{RESET} Scanning for nearby Wi-Fi networks...\n")
    os.system("nmcli dev wifi")

scan_wifi()
