from CSP import *
from ChessState import *


class NBishops:

    def __init__(self, N = 1):
        def leftDiagonalConstraint(state, values, size = N):
            pairs = values.items()
            validStates = list(range(state.state - min(state.state//size, state.state%size)*(size+1), size**2,size + 1))
            validPairs = list(filter(lambda pair: pair[1] and pair[0].state in validStates, pairs))
            statesToConsider = map(lambda x: x[1], validPairs)
            return sum(statesToConsider) <= 1
        def rightDiagonalConstraint(state, values, size = N):
            pairs = values.items()
            validStates = list(range(state.state - min(state.state//size,  (N-1)- state.state% size) * (size-1), size**2,(size-1)))
            validPairs = list(filter(lambda pair: pair[1] and pair[0].state in validStates, pairs))
            statesToConsider = map(lambda x: x[1], validPairs)
            return sum(statesToConsider) <= 1

        self._number = N
        goal = lambda values, size=N:  sum(map(lambda v: v[1], values.items())) == size
        self._CSP = CSP(goal, ChessState(0, set([True,False]),N))

        for i in range(N*N):
            self._CSP.addVariable(ChessState(i, set([True,False]),N))

        self._CSP.addConstraint(leftDiagonalConstraint)
        self._CSP.addConstraint(rightDiagonalConstraint)



    def solve(self):
        return self._CSP.solve()


q = NBishops(15)

soln = q.solve()[0]
print(soln)
