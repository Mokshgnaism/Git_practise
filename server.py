import socket
import threading
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server is listening on port 12345...")
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Client has disconnected.")
                break
            print(f"Received message: {message}")
            response = f"Echo: {message}"
            client_socket.send(response.encode('utf-8'))
        except (ConnectionResetError, ConnectionAbortedError):
            print("Client has disconnected.")
            break
    client_socket.close()
try:
    threads = []
    while True:
        client_socket,addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        t1 = threading.Thread(target=handle_client, args=(client_socket,),daemon=True)
        threads.append(t1)
        t1.start()
except (KeyboardInterrupt, SystemExit, Exception) as e:
    if(e):
        print(f"An error occurred: {e}")
    for t in threads:
        t.exit()
    print("Server is shutting down...")
    server_socket.close()
# first addition to make a merge conflict i will try to know what a merge conflict is and how to resolve it in git
def merge_conflict_example():
    print("This is an example of a merge conflict.")
    handle_client(None)  # This will cause an error since handle_client expects a socket object.