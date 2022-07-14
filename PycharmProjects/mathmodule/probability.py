from abc import ABC  # импорт интерфейсов
from typing import List  # типизация
import math


class IRandomValue(ABC):

    def __init__(self):
        self.xlist = [1]

    def mathexpect(self):  # переопределяется
        pass

    def squaremathexpect(self):  # переопределяется
        pass

    def dispersion(self):  # наследуется
        return self.squaremathexpect() - (self.mathexpect() ** 2)

    def sigma(self):  # наследуется
        return math.sqrt(self.dispersion())

    def get_data(self):  # переопределяется
        pass

    def change_data(self, listt):
        self.xlist = listt
        return self.xlist


class Probability(IRandomValue):
    plist: List[float]
    xlist: List[float]

    def __init__(self):
        self.xlist = [1, 0]
        self.plist = [1.0, 0]

    def mathexpect(self):
        m = 0
        for i in range(len(self.xlist)):
            m += self.xlist[i] * self.plist[i]
        return m

    def squaremathexpect(self):
        msquare = 0
        for i in range(len(self.xlist)):
            msquare += (self.xlist[i] ** 2) * self.plist[i]
        return msquare

    def change_data(self, listx, listp):
        self.xlist = listx
        self.plist = listp
        if len(self.xlist) != len(self.plist):
            raise ValueError("Lists don't seem right")
        if min(self.plist) < 0:
            raise ValueError("P can't be negative")
        if max(self.plist) > 1:
            raise ValueError("P can't be more than 1")
        if sum(self.plist) != 1:
            raise ValueError("It must be full probability")
        return True

    def get_data(self):
        data = [self.xlist, self.plist]
        return data

    def get_x_prabability(self, x):
        i = self.xlist.index(x)
        return self.plist[i]


class Statistic(IRandomValue):
    nlist: List[int]
    xlist: List[float]

    def __init__(self):
        self.xlist = [1]
        self.nlist = [1]

    def mathexpect(self):
        m = 0
        for i in range(len(self.xlist)):
            m += self.xlist[i] * self.nlist[i]
        return m / sum(self.nlist)

    def squaremathexpect(self):
        msquare = 0
        for i in range(len(self.xlist)):
            msquare += (self.xlist[i] ** 2) * self.nlist[i]
        return msquare / sum(self.nlist)

    def change_data(self, listx, listn):
        self.xlist = listx
        self.nlist = listn
        if len(self.xlist) != len(self.nlist):
            raise ValueError("Lists don't seem right")
        if min(self.nlist) < 0:
            raise ValueError("N can't be negative")
        return True

    def get_data(self):
        data = [self.xlist, self.nlist]
        return data

    def get_x_prabability(self, x):
        i = self.xlist.index(x)
        return self.nlist[i]

    def fashion(self):  # новый функционал
        f = self.nlist.index(max(self.nlist))
        return self.xlist[f]
