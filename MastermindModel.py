import copy


class MastermindGame:
    passCode = []  # 4 digits long, 1-9
    correctDigitsRightPlacement = 0
    correctDigitsWrongPlacement = 0

    def getScoreOfGuessCode (self, guessCode):
        self.correctDigitsRightPlacement = self.getCorrectDigitsRightPlacement (guessCode)
        self.correctDigitsWrongPlacement = self.getCorrectDigitsWrongPlacement (guessCode,
                                                                                self.correctDigitsRightPlacement)
        score = 2 * self.correctDigitsRightPlacement + self.correctDigitsWrongPlacement
        return score

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


print ("----- TESTING -----")
print ("Game 1: 1234")
game = MastermindGame ()
game.passCode = [1, 2, 3, 4]
assert game.getScoreOfGuessCode ([1, 2, 3, 4]) == 8
assert game.correctDigitsWrongPlacement == 0
assert game.correctDigitsRightPlacement == 4

assert game.getScoreOfGuessCode ([4, 3, 2, 1]) == 4
assert game.correctDigitsWrongPlacement == 4
assert game.correctDigitsRightPlacement == 0

assert game.getScoreOfGuessCode ([5, 5, 5, 5]) == 0
assert game.correctDigitsWrongPlacement == 0
assert game.correctDigitsRightPlacement == 0

assert game.getScoreOfGuessCode ([1, 1, 2, 2]) == 3
assert game.correctDigitsWrongPlacement == 1
assert game.correctDigitsRightPlacement == 1
print ("All test cases passed. ")
