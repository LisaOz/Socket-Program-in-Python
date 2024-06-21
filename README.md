# Socket-Program-in-Python
This repository contains a socket-based communication program with separate scripts for the server and client. The client reads text messages from an input file and sends them to the server, which logs the received messages.

## Features
Server Script: Listens for incoming connections and logs received messages.
Client Script: Reads messages from an input file and sends them to the server.
Logging: Server logs all received messages for later review.

## Usage
### Running the Server
1. Start the server: python server.py
2. The server will listen on the specified IP and port

### Running the Client
1. Start the client: python client.py
2. The client with send each line from the input file to the server

### Input File
The input file is a text file ('messages.txt') with each line representing messages to the server

### Logging
The server logs messages to 'Communication log' bu default with date and time

### Configuration
Sever and client settings (IP, port, paths) can be configures in the respective scripts



