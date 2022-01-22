import random


class AI:
    def getMove(self, state):  # returns position of the move
        pass


class RandomAI(AI):
    @staticmethod
    def getMove(validMoves):
        if len(validMoves) > 0:
            return random.choice(validMoves)
        else:
            return None

