
class MastermindGame:
    passCode = None #4 digits long, 1-9
    correctDigitsWrongPlacement = None
    correctDigitsRightPlacement = None

    def __init__ (self, passCode):
        self.passCode = passCode

    def guessCode(self, guessCode):
        print(self.passCode)
        #Figure out the number of correctDigitsWrongPlacement
        #figure out the number of correctDigitsRightPlacement
        #return both of those
        #if it's all are correctDigitsRightPlacement then we return a Zero array

