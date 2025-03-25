import os

def create_fake_ap(ssid, interface):
    print(f"{RED}[FAKE AP]{RESET} Creating fake Wi-Fi hotspot: {ssid}")
    os.system(f"airbase-ng -e {ssid} -c 6 {interface}")

create_fake_ap("Free_WiFi", "wlan0mon"
