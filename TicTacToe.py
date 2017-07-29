import sys
from sys import stdout as std

"""
Minimax algorithm to build an tic tac toe AI
-----------------------------------------------
computer represents X and the player is O
so, we are maximiser and the player is minimiser
"""

class board:

    def __init__(self):
        self.positions = []
        self.movesLeft = 9


    def Start(self):
        for i in range(9):
            self.positions.append(0);
    #position value 0 indicates empty space
    #position value 1 indicates X
    #position value -1 indicates O


    def PrintTable(self):
        i = 0;
        for j in range(3):
            for k in range(3):
                if(self.positions[i] == 0):
                     std.write('_ ') #to print without a newline
                elif(self.positions[i] == 1):
                     std.write('X ')
                else:
                     std.write('O ')
                i+=1
            print '\n'


    def NextMove(self,filled):
        self.PrintTable()
        while(True):
            a = input('Enter a number between 0-8')
            if(a > 8 or a < 0):
                continue
            if(not(a in filled)):
                break
        filled.append(a)
        self.positions[a] = -1
        self.movesLeft -= 1


    def GameState(self):
        for row in range (3): #checking for a match in a row
            if( ( self.positions[row*3] == self.positions[row*3+1]) and (self.positions[row*3+1] == self.positions[row*3+2] ) ):
                if(self.positions[row*3] == 1):
                    return 10
                elif(self.positions[row*3] == -1):
                    return -10

        for column in range(3): #match in column
            if((self.positions[column] == self.positions[column + 3]) and (self.positions[column +3] == self.positions[column + 6])):
                if(self.positions[column] == 1):
                    return 10
                elif(self.positions[column] == -1):
                    return -10

        #condition for 2 diagonals
        if((self.positions[0] == self.positions[4]) and (self.positions[4] == self.positions[8])):
            if(self.positions[0] == 1):
                return 10
            elif(self.positions[0] == -1):
                return -10

        if((self.positions[2] == self.positions[4]) and (self.positions[4] == self.positions[6])):
            if(self.positions[2] == 1):
                return 10
            elif(self.positions[2] == -1):
                return -10
        #if none of the above is true
        return 0

    #This function return the best move possible for the given state by the maximiser
    def BestMove(self):
        if(self.movesLeft == 0):
             return -1
        current = -sys.maxint
        for i in range(9):
            if(self.positions[i] == 0):
                self.positions[i] = 1
                if(self.MiniMax(10-self.movesLeft,False) > current):
                    current = self.MiniMax(10-self.movesLeft,False)
                    bestMove = i
                self.positions[i] = 0
        return bestMove

    #This is a recrsive function used to check all posibilities
    def MiniMax(self,depth,MaximisingPlayer):
        #base cases
        score = self.GameState()
        if(score == 10):    #we return score - depth so as to make
                            # that selection which has minimum number of moves
             return (score - depth)
        elif(score == -10):
            return (score + depth)
        elif(depth == 9): #moves finished
            return 0
        #deciding best move from the point of maximising player
        if(MaximisingPlayer):
            curr = -1000
            for i in range(9):
                if(self.positions[i] == 0):
                    self.positions[i] = 1
                    curr = max(curr,self.MiniMax(depth+1,False))
                    self.positions[i] = 0
            return curr
        #Best move from the point of view of minimiser
        else:
            curr = 1000
            for i in range(9):
                if(self.positions[i] == 0):
                    self.positions[i] = -1
                    curr = min(curr,self.MiniMax(depth+1,True))
                    self.positions[i] = 0
            return curr


game = board()
game.Start()
filled = [] #list that stores position occupied
while(game.movesLeft >= 0):
    print game.movesLeft
    game.NextMove(filled)
    a = game.BestMove()
    filled.append(a)
    game.positions[a] = 1
    game.movesLeft -= 1
    b = game.GameState()
    if(b == 10):
        game.PrintTable()
        print 'You lose!\ntry again'
        break
    elif(b == -10):
        game.PrintTable()
        print 'You win!\n'
        break

if(game.movesLeft == -1): #in case of draw
    game.PrintTable()
