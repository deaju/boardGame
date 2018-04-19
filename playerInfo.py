# coding:utf-8
from player import Player
class PlayerInfo():
    def __init__(self,player):
        self.__player = player
        self.__place = -1
        self.__squares = []
        self.__reverse = False

    def getSquareNum(self):
        return len(self.__squares)
    def getPlace(self):
        return self.__place
    def getPlayer(self):
        return self.__player
    def isReverse(self):
        return self.__reverse
    def changeDirection(self):
        self.__reverse = True

    def decideDirection(self):
        self.__reverse = self.__reverse or self.__player.decideDirection()
        
    def decideGetSquare(self,square):
        if self.__player.decideGetSquare() and not square.isGet():
            self.__squares.append(square)
            square.getSquare()

    def isGoal(self):
        return self.__place <0 and self.__reverse

    def setPlace(self,place):
        self.__place = place

    def calcPoint(self):
        if self.isGoal():
            return sum(map(lambda x:x.getPoint(),self.__squares))

