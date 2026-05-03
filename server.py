import socket
import threading
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server is listening on port 12345...")
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit, Exception) as e:
    if(e):
        print(f"An error occurred: {e}")
    print("Server is shutting down...")
    server_socket.close()