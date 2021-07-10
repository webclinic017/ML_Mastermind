import copy


class MastermindGame:
    passCode = []  # 4 digits long, 1-9

    correctDigitsWrongPlacement = 0
    correctDigitsRightPlacement = 0

    def __init__ (self, passCode):
        self.passCode = passCode

    def guessCode (self, guessCode):
        self.correctDigitsRightPlacement = self.getCorrectDigitsRightPlacement (guessCode)
        self.correctDigitsWrongPlacement = self.getCorrectDigitsWrongPlacement (guessCode,
                                                                                self.correctDigitsRightPlacement)

    def getCorrectDigitsRightPlacement (self, guessCode):
        correctDigitsRightPlacement = 0
        if guessCode is None:
            return 0
        for i, digit in enumerate (self.passCode):
            if i >= len (guessCode):
                continue
            else:
                if digit == guessCode [i]:
                    correctDigitsRightPlacement += 1
        return correctDigitsRightPlacement

    def getCorrectDigitsWrongPlacement (self, guessCode, correctDigitsRightPlacement):
        correctDigitsWrongPlacement = 0
        if guessCode is None:
            return 0
        tempGuessCode = copy.deepcopy (guessCode)
        for passDigit in enumerate (self.passCode):
            for guessDigit in enumerate (tempGuessCode):
                if passDigit [1] == guessDigit [1]:
                    correctDigitsWrongPlacement += 1
                    tempGuessCode.remove (guessDigit [1])
                    break
        correctDigitsWrongPlacement -= correctDigitsRightPlacement
        return correctDigitsWrongPlacement


# TEST CODE BELOW
game = MastermindGame ([1, 2, 3, 4])
game.guessCode ([1, 2, 3, 4])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([4, 3, 2, 1])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([5, 5, 5, 5])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([1, 1, 2, 2])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([3, 3, 1, 1])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([4, 4, 4, 4])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([2, 2, 3, 3])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([1, 2, 3])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode ([])
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
game.guessCode (None)
print (str (game.correctDigitsRightPlacement) + " " + str (game.correctDigitsWrongPlacement))
