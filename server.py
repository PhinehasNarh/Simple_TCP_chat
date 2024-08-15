import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=2222):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)
        print(f"Server started on {host}:{port}")
        self.clients = []

    def broadcast(self, message, client_socket):
        print(f"Broadcasting message: {message.decode('utf-8')}")  # Debugging line
        for client in self.clients:
            if client != client_socket:
                try:
                    client.send(message)
                except Exception as e:
                    print(f"Error broadcasting to {client}: {e}")
                    client.close()
                    self.clients.remove(client)

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if not message:
                    print(f"Client {client_socket} disconnected!")
                    break
                self.broadcast(message, client_socket)
            except Exception as e:
                print(f"Error handling client {client_socket}: {e}")
                client_socket.close()
                self.clients.remove(client_socket)
                break

    def start(self):
        while True:
            client_socket, client_address = self.server.accept()
            print(f"Connection established with {client_address}")
            self.clients.append(client_socket)
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()

if __name__ == "__main__":
    chat_server = ChatServer()
    chat_server.start()
