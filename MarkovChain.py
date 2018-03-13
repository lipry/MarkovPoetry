import random
import numpy as np

class MarkovChain:

    def __init__(self):
        self.states = {}

    def add_state(self, state, next):
        if state not in self.states:
            self.states[state] = {}

        values = self.states[state]
        if next in values.keys():
            values[next] = values[next]+1
        else:
            values[next] = 1

        self.states[state] = values

    def get_state(self, t):
        total = sum(self.states[t].values())
        prob = [n/total for n in self.states[t].values()]
        return np.random.choice(list(self.states[t].keys()), 1, p=prob)[0]

    #def generate(self, n_words):
    #    last_kgram = random.choice(self.states.keys())
    #    for i in range(0, n_words):


    @staticmethod
    def leftShift(t, n):
        try:
            n = n % len(t)
        except ZeroDivisionError:
            return tuple()
        return t[n:] + t[0:n]





