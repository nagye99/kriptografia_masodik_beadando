import random

class V_pers:

    def __init__(self, n, x) -> None:
        self.n = n
        self.x = x

    def generateBit(self, t):
        self.c = random.randint(0, 1)
        self.t = t
        return self.c
    
    def check(self, s):
        y = pow(self.x, 2) % self.n
        return pow(s, 2) % self.n == (self.t * pow(y, self.c)) % self.n
