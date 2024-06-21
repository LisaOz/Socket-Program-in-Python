import socket
import logging
import threading

# Configure logging to a shared log file
logging.basicConfig(filename='communication.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def handle_client(data, client_address, server_socket):
    try:
        # Process received data
        logging.info("Received from {}: {}".format(client_address, data.decode('utf-8')))

        # Send response back to client
        server_socket.sendto(b"RESPONSE FROM SERVER", client_address)
    except Exception as e:
        # Print and log the error message if the server fails to start
        print("Error receiving messages from clients:", e)
        logging.error(f"Error during communication with {client_address}: {e}")


def run_server(ip_address, port):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Bind the socket to an IP address and port
        server_socket.bind((ip_address, port))  # bind method used to assign the ip address and a port as a tuple
        print("UDP SERVER STARTED, WAITING FOR MESSAGES...")

        while True:
            # Receive data from a client, handle the data packets
            # recvfrom returns data and client address
            data, client_address = server_socket.recvfrom(1024)
            print("Received message from:", client_address)

            # Create a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(data, client_address, server_socket))
            client_handler.start()
    except Exception as e:
        print("Error while running the server:", e)
        logging.error("Error while running the server: %s", e)

    finally:
        # Close the server socket
        server_socket.close()


if __name__ == "__main__":
    # Connecting to the Localhost
    ip_address = '127.0.0.1'
    port = 5555       # port range 1 to 65535

    # Run the server
    run_server(ip_address, port)