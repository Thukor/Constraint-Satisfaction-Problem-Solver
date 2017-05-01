from CSP import *
from ChessState import *

class NRooks:

    def __init__(self, N = 1):
        def rowConstraint(state, values, size = N):
            pairs = values.items()
            validStates = list(range(state.state//size*size, state.state//size*size+size))
            validPairs = list(filter(lambda pair: pair[1] and pair[0].state in validStates, pairs))

            statesToConsider = list(map(lambda x: x[1], validPairs))
            return sum(statesToConsider) <= 1
        def columnConstraint(state, values, size = N):
            pairs = values.items()
            validStates = list(range(state.state % size, size**2,size))
            validPairs = list(filter(lambda pair: pair[1] and pair[0].state in validStates, pairs))
            statesToConsider = map(lambda x: x[1], validPairs)
            return sum(statesToConsider) <= 1

        self._number = N
        goal = lambda values, size=N:  sum(map(lambda v: v[1], values.items())) == size
        self._CSP = CSP(goal, ChessState(0, set([True,False]),N))

        for i in range(N*N):
            self._CSP.addVariable(ChessState(i, set([True,False]),N))

        self._CSP.addConstraint(rowConstraint)
        self._CSP.addConstraint(columnConstraint)

    def solve(self):
        return self._CSP.solve()


q = NRooks(2)

soln = q.solve()[0]
print(soln)
