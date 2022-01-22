import tkinter as tk
import board
import player


gameWindow = tk.Tk()


game = board.TicTacToe(gameWindow, player.RandomAI, player.RandomAI)

game.start()


gameWindow.mainloop()
