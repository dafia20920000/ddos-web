import socket

def start_c2_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Connection established with {addr}")
        client_socket.send(b"Welcome to C2 Server!\n")
        client_socket.close()

if __name__ == "__main__":
    start_c2_server()
