import socket

def connect_to_c2(host='localhost', port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    message = client.recv(1024)
    print(message.decode("utf-8"))
    client.close()

if __name__ == "__main__":
    connect_to_c2()
