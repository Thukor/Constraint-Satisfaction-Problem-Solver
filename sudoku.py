from collections import Counter
from itertools import *
from time import sleep
import sys
import os
class Sudoku:

    def __init__(self, N, checkBlocks = False):
        self._grid = [['.' for i in range(N)] for i in range(N)]
        self.N = N
        self.domain = [str(i+1) for i in range(N)]
        self.checkBlocks = checkBlocks

    def __str__(self):

        line = ''
        line += "\n" +'-' * (1 + 8 *( self.N // 3) ) + "\n"
        for row in range(0,self.N):
            for column in range(0,self.N):
                if column % 3 == 0: line += '| '
                line += self._grid[row][column] + ' '
            line += '|'

            if row % 3 == 2:
                line += "\n" + '-' * (1 + 8 * ( self.N // 3) )

            line += '\n'
        return line

    def _containsUniqueVals(self, L):
        M = L.copy()
        M = list(filter(lambda x: x != ".", L))
        counts = Counter(M)
        for val, count in counts.items():
            if count > 1:
                return False

        return True

    def isValid(self):

        #Check each row for validity
        for i in range(self.N):
            if not self._containsUniqueVals(self._grid[i]):
                #print("JJSJS")
                return False

        #Check each column for validity
        for i in range(self.N):
            column = [self._grid[j][i] for j in range(self.N)]
            #print(column)
            if not self._containsUniqueVals(column):
                return False

        #Check each 3x3 block
        if self.checkBlocks:
            numBlocks = ( self.N // 3 ) ** 2

            blockStartPoints = {(i//3*3,j//3*3) for i in range(self.N) for j in range(self.N)}

            for (x,y) in blockStartPoints:
                L1 = [self._grid[i][y] for i in range(x,x+3)]
                L2 = [self._grid[i][y+1] for i in range(x,x+3)]
                L3 = [self._grid[i][y+2] for i in range(x,x+3)]

                L = L1 + L2 + L3

                if not self._containsUniqueVals(L):

                    return False

        #Valid
        return True

def _solve(sudoku):

    os.system("clear")
    print(sudoku)
    sleep(.1)
    grid = "".join(["".join(row) for row in sudoku._grid])
    if grid.count(".") == 0:
        return sudoku.isValid()

    for row,col in product(range(sudoku.N), repeat = 2):

        if sudoku._grid[row][col] != ".":
            continue

        for domainVal in sudoku.domain:

            sudoku._grid[row][col] = domainVal
            os.system("clear")
            print(sudoku)
            sleep(.1)
            if sudoku.isValid() and _solve(sudoku):
                return True
            #BackTrack

            sudoku._grid[row][col] = "."
            os.system("clear")
            print(sudoku)
            sleep(.1)

    return False

def solve(sudoku):
    return _solve(sudoku)

if __name__ == "__main__":
    s = Sudoku(int(sys.argv[1]), True)
    solve(s)
