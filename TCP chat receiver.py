import socket
import threading
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.withdraw()  

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Disconnected from server")
                break
            show_popup(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def show_popup(message):
   
    messagebox.showinfo("New Message", message)

if __name__ == "__main__":
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 2222))
        print("Connected to server")

        thread = threading.Thread(target=receive_messages, args=(client_socket,))
        thread.daemon = True
        thread.start()

        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                print("Closing connection")
                client_socket.close()
                break
            client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")

  
    root.mainloop() 