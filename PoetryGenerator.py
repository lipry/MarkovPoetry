from MarkovChain import MarkovChain
import re


class PoetryGenerator:

    def __init__(self, k, n):
        self.mc = MarkovChain()
        self.k = k
        self.n = n

    def train(self, filename):
        file = open(filename)
        words = []
        for line in file:
            #words = words + re.compile("([\w]+|[.,!?;]+|[\n])").findall(line)
            words = words + re.compile("([\w.,!?;']+|[\n])").findall(line)

        print(words)
        for i in range(len(words) - self.k - 1):
            state = tuple(words[i:i+self.k])
            next = words[i+self.k]
            self.mc.add_state(state, next)

    def generate(self):
        state = list(self.mc.get_random_tuple())
        for w in state:
            print("{} ".format(w), end='')

        for i in range(0, self.n):
            gen_word = self.mc.get_state(tuple(state))
            print("{} ".format(gen_word), end='')
            state = self.shift(state, 1)
            state[2] = gen_word

    def shift(self, l, n):
        return l[n:] + l[:n]