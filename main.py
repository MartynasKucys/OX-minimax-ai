import tkinter as tk
import board
import AI

gameWindow = tk.Tk()
# opponent.RandomAI = ai that makes random moves
# opponent.minimaxAI = ai that uses the minimax algorithm
# None = human player
game = board.TicTacToe(gameWindow, None, AI.minimaxAI())

game.start()

gameWindow.mainloop()
