import socket
import threading
import tkinter as tk

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Disconnected from server")
                break
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, message + '\n')
            chat_area.config(state=tk.DISABLED)
            chat_area.yview(tk.END)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_message(event=None):
    message = message_entry.get()
    if message:
        try:
            client_socket.send(message.encode('utf-8'))
            print(f"Sent message: {message}")  # Debugging line
            message_entry.delete(0, tk.END)
        except Exception as e:
            print(f"Error sending message: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TCP Chat System")

    chat_area = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    message_entry = tk.Entry(root)
    message_entry.pack(padx=10, pady=10, fill=tk.X)
    message_entry.bind("<Return>", send_message)

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 2222))
        print("Connected to server")

        thread = threading.Thread(target=receive_messages, args=(client_socket,))
        thread.daemon = True
        thread.start()
    except Exception as e:
        print(f"An error occurred: {e}")

    root.mainloop()
