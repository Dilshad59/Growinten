from scapy.all import sniff, IP, TCP, UDP
import logging
import json
from datetime import datetime

logging.basicConfig(
    filename='packets.log',
    level=logging.INFO,
    format='%(message)s'  
)

def packet_callback(packet):
    packet_data = {}
    
    if IP in packet:
        packet_data['timestamp'] = datetime.now().isoformat()
        packet_data['ip_src'] = packet[IP].src
        packet_data['ip_dst'] = packet[IP].dst
        
        if TCP in packet:
            packet_data['protocol'] = 'TCP'
            packet_data['tcp_sport'] = packet[TCP].sport
            packet_data['tcp_dport'] = packet[TCP].dport
        
        elif UDP in packet:
            packet_data['protocol'] = 'UDP'
            packet_data['udp_sport'] = packet[UDP].sport
            packet_data['udp_dport'] = packet[UDP].dport
        
        else:
            packet_data['protocol'] = 'IP'

        packet_info = json.dumps(packet_data)
        
        print(packet_info)
        logging.info(packet_info)

print("Starting the network sniffer...")
sniff(filter="ip", prn=packet_callback, store=0)
