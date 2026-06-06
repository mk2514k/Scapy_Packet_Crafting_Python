#install scapy
    #pip install scapy

from scapy.all import IP, ICMP, TCP, UDP, send

target = "127.0.0.1"

#ICMP Packet
icmp_packet = IP(dst=target) / ICMP()
send(icmp_packet, verbose=False)
print("ICMP Echo Request sent to", target)

#TCP SYN Packet
tcp_packet = IP(dst=target) / TCP(dport=80, flags="S")
send(tcp_packet, verbose=False)
print("TCP SYN packet sent to", target, "on port 80")

#UDP Packet
udp_packet = IP(dst=target) / UDP(dport=9999)
send(udp_packet, verbose=False)
print("UDP packet sent to", target, "on port 9999")

