# TCP Chat System

This project is a simple TCP-based chat system implemented in Python. It consists of a chat server and a client that can connect to the server to send and receive messages in real-time. The client features a pop-up notification for incoming messages using `tkinter`.

## Features

- **Multi-Client Support**: The server can handle multiple clients simultaneously.
- **Broadcasting**: Messages sent by a client are broadcast to all other connected clients.
- **Pop-Up Notifications**: Clients receive incoming messages through a pop-up window.

## Prerequisites

- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)

## Getting Started

### 1. Clone the Repository


git clone https://github.com/PhinehasNarh/TCP-chat.git
cd TCP-chat

### 2. Run the Server
The server script needs to be running before clients can connect to it.

TCP chat server.py
The server will start and listen for connections on 127.0.0.1 (localhost) and port 2222.

### 3. Run the Client
You can run the client script on the same machine or on a different one that can connect to the server.

TCP chat receiver.py
Once connected, the client will prompt you to enter a message. When another client sends a message, it will be displayed in a pop-up window.

### 4. Sending Messages
After the client connects to the server, you can type messages and press Enter to send them. To exit the chat, type exit and press Enter.

## Code Overview
# Server
chatserver Class: Manages client connections, broadcasts messages, and handles communication.
start() Method: Listens for incoming client connections and starts a new thread for each client.

# Client
receive_messages() Function: Listens for incoming messages from the server and displays them in a pop-up window.
show_popup() Function: Uses tkinter to display incoming messages in a pop-up dialog.


## Customization
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!
