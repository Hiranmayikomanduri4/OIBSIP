import socket
import threading

def receive_messages(sock):
    while True:
        try:
            reply = sock.recv(1024)
            if not reply:
                print("Server disconnected")
                break
            print("Server:", reply.decode())
        except ConnectionResetError:
            print("Connection closed by server")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))
print("Connected to server")

# Start a thread to receive messages
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.start()

# Client input loop
try:
    while True:
        message = input()
        if message.lower() == "exit":
            break
        client_socket.send(message.encode())
except Exception as e:
    print("Client error:", e)
finally:
    client_socket.close()