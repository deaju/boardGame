# coding:utf-8
from square import Square
from random import randint,shuffle

class SquareFactory():
    def createSquares(self,num):
        points = self.__setPoints(num)
        return [Square(i,num) for i in points]

    def __setPoints(self,num):
        start=4*(num-1)
        points = [i for i in range(start,start+4)]
        points.extend([i for i in range(start,start+4)])
        shuffle(points)
        return points