import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print('Server is listening...')

conn, addr = server.accept()

connected = True

while connected:

        msg = conn.recv(2048).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False
            conn.send("GOODBYE".encode(FORMAT))
        else:

            if int(msg) <= 40 :
                conn.send(f"Salary is: {int(msg)*200}".encode(FORMAT))

            else:
                conn.send(f"Salary is :{8000+(int(msg)-40)*300}".encode(FORMAT))
conn.close()
