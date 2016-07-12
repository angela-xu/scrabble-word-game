from helper_functions import *
from user_play import *
import time


#
# #1: Computer chooses a word
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    def new_isValidWord(word, hand):
        word_di = getFrequencyDict(word)
        for i in word_di.keys():
            if hand.get(i, 0) < word_di[i]:
                return False
        return True 

    temp_max_score = 0
    temp_best_word = None
    for word in wordList:
        if new_isValidWord(word, hand) == True:
            s = getWordScore(word, n)
            if s > temp_max_score:
                temp_max_score = s
                temp_best_word = word

    return temp_best_word


#
# #2: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0
    hand_total = 0 
   
    while calculateHandlen(hand) > 0:
        print('Current Hand: '),
        displayHand(hand)
        w = compChooseWord(hand, wordList, n)
        if w == None:
            break
        else:
            s = getWordScore(w, n)
            total += s
            print('"' + w + '"' + ' earned ' + str(s) + ' points.' + ' Total: ' + str(total) + ' points.')    
            hand = updateHand(hand, w)
            print('\n')

    print('Total score: ' + str(total) + ' points.')
    print('')

#
# #3: Playing a game -- both users and computer
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    while True:
        x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if x == 'n':
            hand = dealHand(HAND_SIZE)
            while True:
                y = raw_input('Enter u to have yourself play, c to have the computer play: ')
                print('\n')
                if y == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    print('')
                    break
                elif y == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    print('')
                    break
                else:
                    print('Invalid command.')
        elif x == 'r':
            if hand == {}:
                print('You have not played a hand yet. Please play a hand first!')
                print('')
            else:
                while True:
                    z = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    print('')
                    if z == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif z == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break 
                    else:
                        print('Invalid command.')
        elif x == 'e':
            break
        else:
            print('Invalid command.')

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


