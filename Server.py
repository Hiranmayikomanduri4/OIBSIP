import socket
import threading

def handle_client(conn, addr):
    print("Connected by", addr)
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                print("Client disconnected")
                break
            print("Client:", message)
        except ConnectionResetError:
            print("Client forcibly closed the connection")
            break

    conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)
print("Server listening on port", port)

conn, addr = server_socket.accept()

# Start a thread to handle client messages
thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.start()

# Server input loop
try:
    while True:
        reply = input()
        if reply.lower() == "exit":
            conn.send("Server closed the chat".encode())
            break
        conn.send(reply.encode())
except Exception as e:
    print("Server error:", e)
finally:
    conn.close()
    server_socket.close()