### TCP Chat System
Welcome to my TCP Chat System! This is a simple chat app built in Python using basic TCP/IP and sockets. The chat window has a basic GUI thanks to Tkinter, so you can see and send messages in real-time.

# What You Can Do
Chat with multiple people simultaneously.
See messages pop up in a simple window.
Easy to run—just start the server, then the clients, and you're good to go!

# What You Need
Python 3.x
Just basic Python and some networking knowledge.

# How to Get Started
Clone this Repo
First, grab a copy of the code:
git clone https://github.com/PhinehasNarh/TCP-chat.git

cd TCP-chat

# Run the Server
Fire up the server by running the following in your terminal:
python server.py
If everything's good, you'll see something like:
Server started on 127.0.0.1:2222

# Run the Client
Next, open up another terminal (or multiple if you want to simulate different users), and run:

python client.py

A window will pop up asking for your username and chat room name. After that, you're in!

# Chat Away
Type your message at the bottom of the chat window and hit Enter.

Messages from others will show up in the chat area.

# Troubleshooting Tips
Client can’t connect? Make sure the server is running and is listening on 127.0.0.1:2222.
Socket error [WinError 10048]? This usually means the server’s already running on that port. Make sure it’s not running in another terminal or app.
Not seeing messages? Check the terminals for any error messages. They’ll give you clues on what went wrong. Also, make sure your client and server scripts are talking to each other.

# Limitations
This is just a basic setup. If you’re thinking about using it for more users or heavier traffic, you might want to add more error handling or optimize the code.

# Want to Contribute?
If you have any ideas or improvements, feel free to fork this repo and submit a pull request. I’d love to see what you come up with!

# License
This project is under the MIT License, so feel free to do whatever you like with it.

Coded by: ph1n3y
