class ChessState:

    def __init__(self, state, domain, size = 4):
        self.state = state
        self.domain = domain
        self.size = size

    def successors(self):
        return [ChessState(self.state + 1, self.domain, self.size)] if self.state < (self.size ** 2)-1 else [None]
