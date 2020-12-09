import socket
from tkinter import *
import time

class Client:

    # Global variables for clients, because I will doubt I will change these variables
    header = 64
    port = 8080
    format = 'utf-8'
    disconnect_message = "!DISCONNECT"
    maxConnectAttempt = 5

    def __init__(self, serverIP):

        # Our variables
        self.serverIP = serverIP
        self.addr = (self.serverIP, self.port)

        self.connected = self.connect(self.addr)

        # If cannot connect for whatever reason
        if not self.connected:
            connectAttemptCount = 0
            print(f"[ERROR] Could not connect to {self.addr}")
            while not self.connected and connectAttemptCount < self.maxConnectAttempt:
                self.connected = self.connect(self.addr)
                connectAttemptCount += 1
                print(f"[RETRYING] to connect to {serverIP}\n[RETRY_COUNT] {connectAttemptCount}")

                # If the connected state has changed or max amount of retries
                if self.connected:
                    print(f"[CONNECTED] Connected to {serverIP}")
                    break
                elif connectAttemptCount == self.maxConnectAttempt:
                    print(f"[FAIL] Failed to connect to {self.addr}")
                    break

        elif self.connected:
            print(f"[CONNECTED] Connected to {self.addr}")

    # Connect function
    def connect(self, addr):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(addr)
            return True
        except:
            return False

    def send(self, msg):

        # Sends a message to the server
        message = msg.encode(self.format)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.format)
        send_length += b' ' * (self.header - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        receivedMessage = (self.client.recv(2048).decode(self.format))

        return receivedMessage

    def decode_message(self, message):
        pass


class Boot:
    def __init__(self):

        self.client = False


        self.bootUp = Tk()
        self.bootUp.geometry("150x100")

        self.loadingLabel = Label(self.bootUp, text="CONNECTING")
        self.loadingLabel.pack()

        self.warningLabel = Label(self.bootUp, text="Do not shut this window")
        self.warningLabel.pack()

        self.loaded = self.loadingLabel.after(2000, self.ready_to_load)

        self.proceedButton = ""

        self.bootUp.mainloop()

    def ready_to_load(self):
        self.client = Client("192.168.0.20")

        if self.client.connected:
            self.loadingLabel.config(text="LOADING - CONNECTED")
            self.warningLabel.destroy()
            self.proceedButton = Button(self.bootUp, text="PROCEED", command=self.login_call)
            self.proceedButton.pack()
            return True
        elif not self.client.connected:
            self.loadingLabel.config(text="FAIL")
            self.warningLabel.config(text="Retry Connecting?")
            self.proceedButton = Button(self.bootUp, text="Retry To Connect", command=self.retry_connect)
            self.proceedButton.pack()

    def login_call(self):
        self.bootUp.destroy()

    def retry_connect(self):
        self.loadingLabel.config(text="RETRYING TO CONNECT")
        self.warningLabel.config(text="Do not shut this window")
        self.proceedButton.destroy()

        self.warningLabel.after(1000, self.ready_to_load)


if __name__ == "__main__":
    print("[ERROR] Cannot run without app")
else:
    try:
        bootup = Boot()
        client = bootup.client
    except:
        print(sys.exit("[ERROR] Client cannot run"))
