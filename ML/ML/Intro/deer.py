import random

class population(object):
    def __init__(self):
        self.pop = [randint(6,30), randint(6,30), randint(6,30), randint(6,30), randint(6,30), randint(6,30)]
        self.total = 0
        for i in self.pop:
            self.total += i
        self.year = 0

    def survivalRates(self):
        for i in range(len(self.pop)):
            if i == 0 or i == 1:
                self.pop[i] *= .95
            if i == 2 or i == 3:
                self.pop[i] *= .85
            else:
                self.pop[i] *= .7
        for i in self.pop:
