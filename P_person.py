import random

class P_pers:

    def __init__(self, n, x) -> None:
        self.n = n
        self.x = x

    def generateT(self):
        self.r = random.randrange(1, self.n)
        t = (self.r * self.r) % self.n
        return t

    def calculateChecker(self, c):
        s = self.r * pow(self.x, c)
        return s