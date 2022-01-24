import random


class AI:
    @staticmethod
    def getMove(validMoves, state, isXTurn):  # returns position of the move
        pass


class RandomAI(AI):
    @staticmethod
    def getMove(validMoves, state, isXTurn):
        if len(validMoves) > 0:
            return random.choice(validMoves)
        else:
            return None


class __minimaxAI(AI):
    def getMove(self, validMoves, state, isXTurn):

        if len(validMoves) == 9:  # on first turn pick a random move
            return random.choice(validMoves)

        tree = self.__generateTree(state, isXTurn)
        a = self.__miniMax(tree)
        return a

    def __generateTree(self, currentGameState, isXTurn):
        root = Tree()
        root.isMaximising = isXTurn
        root.state = currentGameState
        # for each free space add child
        for i in range(len(root.state)):
            if root.state[i] == "_":

                nextGameState = self.__replaceChar(
                    root.state, i, "X" if isXTurn else "O"
                )
                nextPosScore = self.__evaluateGameState(nextGameState)

                if nextPosScore == None:  # no winner
                    if "_" not in nextGameState:
                        leaf = Tree()  # full board no winner
                        leaf.score = 0
                        leaf.state = nextGameState
                        root.children.append(leaf)
                    else:
                        root.children.append(
                            self.__generateTree(nextGameState, not root.isMaximising)
                        )
                else:
                    leaf = Tree()
                    leaf.score = nextPosScore
                    leaf.state = nextGameState
                    root.children.append(leaf)

        return root

    def __findDifference(self, firstState, secondState):

        for i in range(len(firstState)):
            if firstState[i] != secondState[i]:
                return i

    def __miniMax(self, root):

        childrenScores = list()
        for child in root.children:
            childrenScores.append(self.__getMiniMaxScore(child))

        valueToFind = max(childrenScores) if root.isMaximising else min(childrenScores)

        nextStateIndex = childrenScores.index(valueToFind)
        nextState = root.children[nextStateIndex].state
        return self.__findDifference(root.state, nextState)

    def __getMiniMaxScore(self, root):
        if root.score == None:

            childScores = list()

            for child in root.children:
                if child.score == None:
                    childScores.append(self.__getMiniMaxScore(child))
                else:
                    childScores.append(child.score)

            return max(childScores) if root.isMaximising else min(childScores)

        else:
            return root.score

    @staticmethod
    def __replaceChar(string, pos, char):
        return string[:pos] + char + string[pos + 1 :]

    def __evaluateGameState(self, gameState):
        # f(x) = (number_of_free_spaces + 1) * \[+/-\](based on who won the game)
        # method returns None if no winner or number if there is

        if self.__allCharactersSame(gameState[:3]):
            return self.__getWinner(gameState[:3], gameState)
        if self.__allCharactersSame(gameState[3:6]):
            return self.__getWinner(gameState[3:6], gameState)
        if self.__allCharactersSame(gameState[6:]):
            return self.__getWinner(gameState[6:], gameState)

        if self.__allCharactersSame(gameState[0] + gameState[4] + gameState[8]):
            return self.__getWinner(
                gameState[0] + gameState[4] + gameState[8], gameState
            )
        if self.__allCharactersSame(gameState[2] + gameState[4] + gameState[6]):
            return self.__getWinner(
                gameState[2] + gameState[4] + gameState[6], gameState
            )

        if self.__allCharactersSame(gameState[0] + gameState[3] + gameState[6]):
            return self.__getWinner(
                gameState[0] + gameState[3] + gameState[6], gameState
            )
        if self.__allCharactersSame(gameState[1] + gameState[4] + gameState[7]):
            return self.__getWinner(
                gameState[1] + gameState[4] + gameState[7], gameState
            )
        if self.__allCharactersSame(gameState[2] + gameState[5] + gameState[8]):
            return self.__getWinner(
                gameState[2] + gameState[5] + gameState[8], gameState
            )

        return None  # no winner

    def __getWinner(self, winningString, currentGameSate):
        if winningString[0] == "X":
            return self.__countTheSame(currentGameSate, "_") + 1
        if winningString[0] == "O":
            return (self.__countTheSame(currentGameSate, "_") + 1) * -1

    @staticmethod
    def __allCharactersSame(s):
        n = len(s)
        for i in range(1, n):
            if s[i] != s[0]:
                return False
        return True

    @staticmethod
    def __countTheSame(string, char):
        count = 0
        for charecter in string:
            if charecter == char:
                count += 1
        return count


class Tree:
    def __init__(self):
        self.children = list()
        self.state = None

        self.score = None
        self.isMaximising = None
