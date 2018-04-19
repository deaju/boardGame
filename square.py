# coding:utf-8

class Square():
    def __repr__(self):
        return "{point: "+str(self.__point)+ ", isGet: "+ str(self.__isGet)+", isEmpty: "+str(self.isEmpty())+"}" 
    def __init__(self,point,squareType):
        self.__point=point
        self.__isGet=False
        self.__squareType=squareType
        self.__player=None

    def getPoint(self):
        return self.__point
    def getSquare(self):
        self.__isGet=True
    def isGet(self):
        return self.__isGet
    def isEmpty(self):
        return self.__player == None
    def setPlayer(self,player):
        self.__player = player
    def movePlayer(self):
        self.__player = None
    def printBoard(self):
        if self.isEmpty():
            if self.__isGet:
                return 'non'
            else:
                return str(self.__squareType)
        else:
            return self.__player.printBoard()