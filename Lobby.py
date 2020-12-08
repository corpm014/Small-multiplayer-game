from tkinter import *
import numpy as np


class Game:
    maxPlayers = 2

    def __init__(self, gameName, playerHost):
        self.gameName = gameName
        self.playerHost = playerHost
        self.players = np.array([])

    def add_player(self, player):
        if len(self.players) < 2 and player not in self.players:
            newPlayer = np.append(self.players, player)
            self.players = newPlayer
            return True
        else:
            return False

    def remove_player(self, player):
        removePlayer = np.delete(self.players, [x for x in range(len(self.players)) if self.players[x] == player])
        self.players = removePlayer


class Lobby:
    maxGames = 4

    def __init__(self):
        self.games = np.array([])
        self.lobbyPlayers = np.array([])

    def add_game(self, game):
        if type(game) == Game and len(self.games) < 4:
            newGame = np.append(self.games, game)
            self.games = newGame
            print(f"[ADDED Game {game}, has been added")
            return True
        else:
            print(f"[ERROR] Game {game}, has not been added")
            return False

    def remove_game(self, game):
        removeGame = np.delete(self.games, [x for x in range(len(self.games)) if self.games[x] == game])
        self.games = removeGame

    def add_player_to_lobby(self, player):
        if len(self.lobbyPlayers) < 2 and player not in self.lobbyPlayers:
            newPlayer = np.append(self.lobbyPlayers, player)
            self.lobbyPlayers = newPlayer
            return True
        else:
            return False

    def remove_player_from_lobby(self, player):
        removePlayer = np.delete(self.lobbyPlayers, [x for x in range(len(self.lobbyPlayers)) if self.lobbyPlayers[x] == player])
        self.lobbyPlayers = removePlayer


class LobbyGUI:
    def __init__(self, GUI, app):

        # These are where we get the data from and also the create the GUI
        self.GUI = GUI
        self.app = app

        if type(app) == Lobby:
            for game in self.app.games:
                self.display_games(game=game, client=1)

        # Assuming that self.GUI is a type <class 'Tk'>
        self.GUI.mainloop()

    def display_games(self, client, game):
        displayGame = Label(self.GUI, text=game.gameName)
        displayGame.pack()
        joinButton = Button(self.GUI, text="Join", command=lambda: self.join(client, game))
        joinButton.pack()

    def join(self, client, game):
        print(client, game.gameName)

if __name__ == "__main__":
    mainLobby = Lobby()
    root = Tk()

    game1 = Game("1", "1")
    game2 = Game("2", "2")

    mainLobby.add_game(game1)
    mainLobby.add_game(game2)

    mainGUI = LobbyGUI(root, mainLobby)