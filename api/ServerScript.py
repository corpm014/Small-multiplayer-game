import socket
import threading
from Game import Lobby as Lb
import numpy as np

localLobby = Lb.Lobby()

class Server:
    
    port = 8080
    header = 64
    serverIP = socket.gethostbyname(socket.gethostname())
    format = 'utf-8'
    disconnectMessage = "!DISCONNECT"

    def __init__(self):
        # Information on the server
        self.address = (self.serverIP, self.port)

        # Creating the server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.clients = np.array([])


    def handleClient(self, client, addr):
        print(f"[NEW CONNECTION] {addr}")

        connected = True

        # The receiving message loop
        while connected:
            msg_length = client.recv(self.header).decode(self.format)

            # If the message is valid
            if msg_length:
                msg_length = int(msg_length)
                msg = client.recv(msg_length).decode(self.format)

                if msg == self.disconnectMessage:
                    removeCLient = np.delete(self.clients, [x for x in range(
                        0, len(self.clients)) if self.clients[x] == client])
                    self.clients = removeCLient
                    print(f"[!DISCONNECT] Client {client} disconnected")
                    print(f"[ACTIVE CONNECTIONS] {len(self.clients)}")
                else:
                    print(f"[{addr}] {msg}")
        client.close()


    # Method to start the server
    def startServer(self):
        print("[STARTING] Server is starting")

        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.serverIP}")

        # Accepts incoming connections
        while True:
            client, addr = self.server.accept()
            newClient = np.append(self.clients, client)

            self.clients = newClient

            # Start this process on a new thread for concurrency
            thread = threading.Thread(
                target=self.handleClient, args=(client, addr))

            # Actually start the thread
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {len(self.clients)}")


    def sendMessage(self, message, client):
        print(f"[SENDING] Sending a message to {client}")
        client.send(message)


    def decodeMessage(self, message, client):
        # All the conditions that we will receive
        if message == "CREATE":
            self.sendMessage("GAME_INFO", client)
        elif message == "LOGIN":
            self.sendMessage("USER_INFO", client)
        elif message == "SIGN_UP":
            self.sendMessage("SIGN_INFO", client)


# Main program runner
if __name__ == "__main__":
    try:
        MainServer = Server()
        MainServer.start_server()
    except Exception as e:
        print(sys.exit("[ERROR] Server cannot start", e))
