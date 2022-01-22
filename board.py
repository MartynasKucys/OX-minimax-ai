from tkinter import *
from events import Events


# ? "__funcName" to make it a private function

# state is a string of 1s and 0s
# 1 = X
# 0 = O
# _ = None
class TicTacToe:

    positions = list()
    state = "_________"
    XTurn = True
    buttonWidth = 7
    buttonHeight = 5
    gameEnded = False
    buttonsUnlocked = False
    events = Events()

    # None payer = human
    def __init__(self, window, XPlayer, OPlayer):

        window.title("TicTacToe")

        self.gameSpace = Frame(window)
        self.gameSpace.grid(row=0, column=0)

        self.mainButtonFrame = Frame(self.gameSpace)
        self.mainButtonFrame.grid(row=0, column=0)
        self.__createMainButtons(self.mainButtonFrame)

        self.bottomFrame = Frame(self.gameSpace)
        self.bottomFrame.grid(row=1, column=0, sticky="nsw")
        self.__createBottom(self.bottomFrame)

        self.XPlayer = XPlayer
        self.OPlayer = OPlayer

    def start(self):

        while not self.gameEnded:
            if self.XTurn:
                # X turn
                self.__setPosition(
                    self.XPlayer.getMove(self.__getValidMoveIndexes()), "X"
                )
                # check if game ended
                if self.checkIfGameEnded():
                    break
                self.XTurn = False
            else:
                # O turn

                self.__setPosition(
                    self.OPlayer.getMove(self.__getValidMoveIndexes()), "O"
                )
                # check if game ended
                if self.checkIfGameEnded():
                    break
                self.XTurn = True

    def __XWon(self):
        self.consoleVar.set("X won")
        self.gameEnded = True
        return True

    def __OWon(self):
        self.consoleVar.set("O won")
        self.gameEnded = True
        return True

    def __noOneWon(self):
        self.consoleVar.set("Draw")
        self.gameEnded = True
        return True

    def findWhoWon(self, string):
        if "X" in string:
            return self.__XWon()
        elif "O" in string:
            return self.__OWon()

    def checkIfGameEnded(self):
        if self.__allCharactersSame(self.state[:3]):  # top row
            print(self.state[:3] + "1")
            self.findWhoWon(self.state[:3])
        elif self.__allCharactersSame(self.state[3:6]):  # middle row
            print(self.state[3:6] + "2")
            self.findWhoWon(self.state[3:6])
        elif self.__allCharactersSame(self.state[6:]):  # bottom row
            print(self.state[6:] + "3")
            self.findWhoWon(self.state[6:])
        elif self.__allCharactersSame(
            (self.state[0] + self.state[4] + self.state[8])
        ):  # left to right diagonal
            print((self.state[0] + self.state[4] + self.state[8]) + "4")
            self.findWhoWon((self.state[0] + self.state[4] + self.state[8]))
        elif self.__allCharactersSame(
            (self.state[2] + self.state[4] + self.state[6])
        ):  # right to left diagonal
            print((self.state[2] + self.state[4] + self.state[6]) + "5")
            self.findWhoWon((self.state[2] + self.state[4] + self.state[6]))
        elif self.__allCharactersSame(
            self.state[0] + self.state[3] + self.state[6]
        ):  # left column
            print(self.state[0] + self.state[3] + self.state[6] + "6")
            self.findWhoWon(self.state[0] + self.state[3] + self.state[6])
        elif self.__allCharactersSame(
            self.state[1] + self.state[4] + self.state[7]
        ):  # middle column
            print(self.state[1] + self.state[4] + self.state[7] + "7")
            self.findWhoWon(self.state[1] + self.state[4] + self.state[7])
        elif self.__allCharactersSame(
            self.state[2] + self.state[5] + self.state[8]
        ):  # right column
            print(self.state[2] + self.state[5] + self.state[8] + "8")
            self.findWhoWon(self.state[2] + self.state[5] + self.state[8])
        elif "_" not in self.state:
            # full board nobody won
            print(self.state)
            return self.__noOneWon()

        else:
            return False

    def __allCharactersSame(self, s):
        n = len(s)
        for i in range(1, n):
            if s[i] != s[0]:
                return False
        return True

    def __change(self, position):
        if self.buttonsUnlocked:
            self.positions[position].set(position)
            self.buttonsUnlocked = False

    def __createMainButtons(self, frame):
        for row in range(3):
            for column in range(3):
                strVar = StringVar()
                button = Button(
                    frame,
                    textvariable=strVar,
                    width=self.buttonWidth,
                    height=self.buttonHeight,
                    command=lambda pos=row * 3 + column: self.__change(pos),
                )
                button.grid(row=row, column=column)
                self.positions.append(strVar)

    def __reset(self):
        # reset board
        # --buttons
        for position in self.positions:
            position.set("")
        # --state
        self.state = "_________"
        # reset turn order
        self.XTurn = True
        # reset conole var
        self.consoleVar.set("")
        # reset gemeEnded
        self.gameEnded = False
        self.start()

    def __createBottom(self, frame):

        self.resetButton = Button(
            frame,
            width=self.buttonWidth,
            height=(int)((self.buttonHeight) / 2),
            text="Reset",
            command=self.__reset,
        )
        self.resetButton.grid(row=0, column=0, sticky="nsew", rowspan=2)

        self.consoleVar = StringVar()
        self.consoleVar.set("~sample~")
        self.consoleLabel = Label(frame, textvariable=self.consoleVar)
        self.consoleLabel.grid(row=0, column=1, rowspan=2)

    def __setPosition(self, position, symbol):
        self.positions[position].set(symbol)
        self.state = self.state[:position] + symbol + self.state[position + 1 :]

    def __getValidMoveIndexes(self):
        indexes = list()
        for i in range(len(self.state)):
            if self.state[i] == "_":
                indexes.append(i)
        return indexes

