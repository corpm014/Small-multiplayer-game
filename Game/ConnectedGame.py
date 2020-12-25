from tkinter import *
import sys


# Game once connected
class ConnectedGame:
    def __init__(self, client1, client2):
        self.client1 = client1
        self.client2 = client2


# The game GUI
class ConnectedGameGui:
    def __init__(self, app):
        if type(app) == ConnectedGame:
            self.app = app
        else:
            print("[CONNECTED GAME IMPORT ERROR] Game is not type ConnectedGame")


# Program run
if __name__ == '__main__':
    print(sys.exit("[ERROR] Cannot run without server support"))
else:
    pass