from MastermindModel import MastermindGame


class MastermindGenetics:
    MAX_SCORE = 8
    MAX_ROUNDS = 10
    FIRST_CODE = 1111
    LAST_CODE_ADD_ONE = 9999

    def calculateFitness (self, totalScore, guessCount):
        averageScorePerGuess = totalScore / guessCount
        fitness = averageScorePerGuess / self.MAX_SCORE
        return fitness

    def calculateFitnessForRound (self, mastermindGame):
        totalScoreForRound = 0
        totalGuesses = 0
        for x in range (0, self.MAX_ROUNDS):
            # need to
            totalScoreForRound += mastermindGame.getScoreOfGuessCode (
                #     need to write the method that generates the guessCodes
            )
            totalGuesses += 1
            if totalScoreForRound == 8:
                break
        return self.calculateFitness (totalScoreForRound, totalGuesses)

    def calculateOverallFitness (self):
        cumulativeFitness = 0
        game = MastermindGame ()
        for passCode in range (self.FIRST_CODE, self.LAST_CODE_ADD_ONE):
            game.passCode = [int (digit) for digit in str (passCode)]
            cumulativeFitness += self.calculateFitnessForRound (game)
        totalRounds = self.LAST_CODE_ADD_ONE - self.FIRST_CODE
        return cumulativeFitness / totalRounds
