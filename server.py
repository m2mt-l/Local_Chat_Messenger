import socket, os
from faker import Faker


sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = "./socket_file"

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"starting up on {server_address}")
sock.bind(server_address)

while True:
    print("\nwaiting to receive messages")
    data, address = sock.recvfrom(4096)
    fake = Faker()

    print(f"received {len(data)} bytes from {address}")

    if fake:
        if int(data) == 1:
            response = fake.name()
        elif int(data) == 2:
            response = fake.address()
        else:
            response = fake.text()
        sent = sock.sendto(response.encode("utf-8"), address)
        print(f"sent {sent} bytes back to {address}")
