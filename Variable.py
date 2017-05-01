class Variable:

    def __init__(self, state, domain,successorFunc):

            self._successorFunc = successorFunc
            self._state = state
            self._value = value
            self._domain = domain

    def successors(self):
        return self._successorFunc()

    @property
    def domain(self): return self._domain

    @property
    def value(self):  return self._value

    @property
    def state(self):  return self._state

    @value.setter
    def value(self, newVal):
        self._value = newVal
