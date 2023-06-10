import socket, os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = "./socket_file"
address = "./client_socket_file"

while True:
    message = input("This is a local chat messenger app! Please choose a response type you would like to receive.\n1: name\n2: address\n3: text\n")
    if 1 <= int(message) <= 3:
        break
    else:
        print("\nInvalid input. Please try again.\n")

try:
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)

try:
    sent = sock.sendto(message.encode("utf-8"), server_address)

    print("\nwaiting to receive")
    data, server = sock.recvfrom(4096)
    data_str = data.decode("utf-8")
    print(f"received \"{data_str}\"")

finally:
    print("closing socket")
    sock.close()
