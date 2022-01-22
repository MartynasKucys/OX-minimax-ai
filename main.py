import tkinter as tk
import board
import player

gameWindow = tk.Tk()
# player.RandomAI = ai that makes random moves
# player.minimaxAI = ai that uses the minimax algorithm
# None = human player
game = board.TicTacToe(gameWindow, None, None)

game.start()

gameWindow.mainloop()
