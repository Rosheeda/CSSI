
 def initWord(word):
     temp = []
     for i in word:
         temp.append('_')
     return temp

 def printBoard(board,guessList):
     print " ".join(board)
     print "Guesses: " + " ".join(guessList)

 def addGuess(board,word,guess):
     for i in range(len(word)):
         if guess == word[i]:
             board[i] = guess

 def game():
    chosenWord = "programming".lower()
    guesses = []
    board = initWord(chosenWord)

    while '_' in board:
      guess = raw_input('Enter a letter: ').lower()

      if len(guess) == 1:
        if guess in chosenWord:
            for i in range(len(chosenWord)):
                if guess == chosenWord[i]:
                   board[i] = guess
        guesses.append(guess)
