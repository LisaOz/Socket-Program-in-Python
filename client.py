import socket
import logging
import threading


# Configure logging
logging.basicConfig(filename='communication.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def run_client(client_id, server_ip, server_port, input_file):
    # Creating a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        with open(input_file, 'r') as file:  # read the messages from the input file
            messages = file.readlines()

            # Loop for multiple messages/users
            for message in messages:
                # Send the message to the server
                client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))

                # Log the message
                logging.info(f"Client {client_id} sent to server ({server_ip}:{server_port}): {message.strip()}")

                # Receive response from server
                data, _ = client_socket.recvfrom(1024)
                print(f"Client {client_id} received from server: ", data.decode('utf-8'))

                # Log the server's response
                logging.info(f"Client {client_id} received from server ({server_ip}:{server_port}:{data.decode('utf-8')})")
    except Exception as e:
        print("Error sending/receiving message:", e)
        logging.error(f"Error sending/receiving message:, {e}")
    finally:
        # Close the socket
        client_socket.close()


def start_clients(num_clients, server_ip, server_port, input_file):
    threads = []
    for i in range(num_clients):
        thread = threading.Thread(target=run_client, args=(i, server_ip, server_port, input_file))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # Target IP address and port
    ip_address = '127.0.0.1'
    port = 5555

    # Input_file containing messages
    input_file = 'messages.txt'

    # Run the client
    start_clients(10, ip_address, port, input_file)