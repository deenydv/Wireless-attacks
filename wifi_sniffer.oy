from scapy.all import *

def packet_sniffer(interface):
    print(f"{YELLOW}[INFO]{RESET} Sniffing Wi-Fi packets on {interface}...\n")
    sniff(iface=interface, prn=lambda pkt: pkt.summary(), store=False)

packet_sniffer("wlan0mon")
