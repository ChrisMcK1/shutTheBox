#! /usr/bin/python3

import random
import sys #to trigger game over for incorrect input
import time

#setting up the Board to show which number slot we're in, which will have an integer
#until it is selected by the user to be removed from the board, then it will be 'X'

##Need to add """ """ notation to functions

theBoard = [1, 2, 3,4,\
            5, 6, 7, 8, 9, \
            10]

#defining function for the visual of the board, starts with showing each integer 1 thru 10

def printBoard(board):
    print(str(board[0]) + '|' + str(board[1]) + '|' + str(board[2]) + '|' \
          + str(board[3]) + '|' + str(board[4]) + '|' + str(board[5]) + '|' \
          + str(board[6]) + '|' + str(board[7]) + '|' + str(board[8]) + '|' \
          + str(board[9]) + '|')



def winCon():
    if theBoard == ['X', 'X', 'X','X',\
            'X', 'X', 'X', 'X', 'X', \
            'X']:
        print('Congratulations, you\'ve won!')
        time.sleep(2)
        print('Goodbye!')
        

def diceRollFunc():
    while theBoard != ['X', 'X', 'X','X',\
            'X', 'X', 'X', 'X', 'X', \
            'X']:
        diceRoll = random.randint(1, 6) + random.randint(1,6)
        while True:
            print('Roll the pair of dice by typing \'r\'.')
            roll = input()
            if roll == ('r'):
                print('You rolled a ' + str(diceRoll) + '.  Now choose which \
numbers to remove from the board.')
                print('Here\'s the board again, enter one number \
to at a time to remove it from the board.')
            printBoard(theBoard)
            newBoard = input()
            newBoard1 = 0
            newBoard2 = 0
            newBoard3 = 0
            try:
                if int(newBoard) != int(theBoard[int(newBoard)-1]):   #test to check if input is an available space on board and not already an 'X'
                    continue
            except ValueError:
                print('That is an invalid input, start over.')
                sys.exit()
            except IndexError:
                print('That is an invalid input, start over.')
                sys.exit()
            if int(newBoard) > 0 and int(newBoard) < 11 and int(newBoard) <= diceRoll:
                theBoard[int(newBoard)-1] = 'X'
            if (int(diceRoll) - int(newBoard)) == 0:
                break
            if int(newBoard) > int(diceRoll):
                print('That is an invalid input, start over.')
                sys.exit()
            if (int(diceRoll) - int(newBoard)) != 0:
                print('Please enter another number to remove')
                newBoard1 = input()
                theBoard[int(newBoard1)-1] = 'X'
            if (int(newBoard1) + int(newBoard)) > diceRoll:
                print('That is an invalid input, start over.')
                sys.exit()
            if (int(diceRoll) - int(newBoard) - int(newBoard1)) == 0:
                break
            if (int(diceRoll) - int(newBoard) - int(newBoard1)) != 0:
                print('Please enter another number to remove')
                newBoard2 = input()
                theBoard[int(newBoard2)-1] = 'X'
            if (int(newBoard1) + int(newBoard2) + int(newBoard)) > diceRoll:
                print('That is an invalid input, start over.')
                sys.exit()
            if (int(diceRoll) - int(newBoard) - int(newBoard1) - int(newBoard2)) == 0:
                break
            if (int(diceRoll) - int(newBoard) - int(newBoard1) - int(newBoard2)) != 0:
                print('Please enter another number to remove')
                newBoard3 = input()
                theBoard[int(newBoard3)-1] = 'X'
            if (int(newBoard1) + int(newBoard2) + int(newBoard3) + int(newBoard)) > diceRoll:
                print('That is an invalid input, start over.')
                sys.exit()
            if (int(diceRoll) - int(newBoard) - int(newBoard1) - int(newBoard2) - int(newBoard3)) == 0:
                break
            
            #Need to define function or statement that will check if current dice roll is playable on the available board integer spaces in the list, if not, the game needs to end.
            
        printBoard(theBoard)
        
        




print('Welcome to Shut the Box! Here is your board, let\'s get started.')


printBoard(theBoard)

diceRollFunc()

       
winCon()


