from collections import namedtuple
from collections import defaultdict
import time
import os

Variable = namedtuple("Variable", "state domain successorFunc")
def createGrid(numPieces):
    grid = list()
    for i in range(0,6*numPieces+1):
        if i == 0:
            line = '┌'
            for j in range(0,numPieces-1):
                line += '─'*7 + '┬'
            line += '─'*7 + '┐'
            grid.append(list(line))
            # print('\t\t\t\t' + line)
        elif i == 6*numPieces:
            line = '└'
            for j in range(0,numPieces-1):
                line += '─'*7 + '┴'
            line += '─'*7 + '┘'
            grid.append(list(line))
            # print('\t\t\t\t' + line)
        elif i % 6 == 0:
            line = '├' + '─'*7
            for j in range(0,numPieces-1):
                line += '┼' + '─'*7
            line += '┤'
            grid.append(list(line))
            # print('\t\t\t\t' + line)
        else:
            line = '│'
            for j in range(0,numPieces):
                line +=  ' '*7 + '│'
            grid.append(list(line))
            # line += '│'
            # print('\t\t\t\t' + line)

    return grid

def modifyGrid(grid, state, chessPiece = 'Q'):
    row = state[0]
    col = state[1]
    grid[3 + 6*row][4 + 8*col] = chessPiece

def updateGrid(grid, states, chessPiece = 'Q'):
    for state in states:
        modifyGrid(grid, state, chessPiece)

def printGrid(grid, tabCount):
    string = ""
    for line in grid:
        string += "\t" * (tabCount) + ''.join(line) + '\n'
        #print('\t\t\t' + string)
    return string


# if __name__ == "__main__":
#     print("WELCOME TO OUR SIMULATION")
#     chessPiece = input("Type in your choice of chess piece from:\n\tQueen\n\tBishop\n\tRook\n\n")[0].upper()
#     numPieces = int(input("\nType in the number of pieces you want:\n"))
#
#     # print("\nHere's a grid of the chess board for your pleasure\n")
#     # print('┌ ────────── ┐')
#     # print('│ d │   │  │')
#     # print('├ ───┤')
#     # print('└')
#     # print('┘')
#     # print('─')
#     # print('┤')
#     # print('┬')
#     # print('┼')
#     # print('┴')
#
#     grid = createGrid(numPieces)
#     modifyGrid(grid, (2,1), chessPiece)
#     printGrid(grid)


class CSPChess:

    """
    Constructor for arbitrary Constraint Satisfaction Problem

    @param variables :  Set of Variables for a CSP
    @param constraints :  Set of Constraints for a CSP
    @modifies None
    @effects  Creates a new CSP Object
    @returns None

    """

    def __init__(self,goalFunc, startState,size, variables = None, constraints = None):
        self._variables = [] if not variables else variables
        self._constraints = [] if not constraints else constraints
        self._goalFunc = goalFunc
        self._startState = startState
        self._size = size

    def addVariable(self, variable):
        self._variables.append(variable)

    def addConstraint(self, constraint):
        self._constraints.append(constraint)

    def solved(self, values):
        return self._goalFunc(values)

    def _solveHelper(self,state, states, solution, grid):

        validPairs = list(map(lambda x: (x[0].state // self._size, x[0].state % self._size),filter(lambda x: x[1], states.items())))
        ngrid = createGrid(self._size)
        updateGrid(ngrid,validPairs)
        ngrid = printGrid(ngrid, 4)

        if ngrid != grid:
            #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            os.system('clear')
            print(ngrid)
        time.sleep(.1)

        if self.solved(states):
            return True,solution

        for successor in state.successors():
            if not successor:
                return False, solution
            for domainVal in successor.domain:
                prev = states[successor]
                states[successor] = domainVal
                consistent = all([c(successor, states) for c in self._constraints])

                if(consistent):
                    result = self._solveHelper(successor, states, solution, ngrid)
                    if result[0]:  return result
                states[successor] = prev

        return False,solution

    def solve(self):
        return self._solveHelper(self._startState, defaultdict(lambda: False), [], "")
