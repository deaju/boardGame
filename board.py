# coding:utf-8
from squareFactory import SquareFactory
from dice import Dice
from playerInfo import PlayerInfo
from player import Player

class Board():
    def __init__(self,players):
        self.__squares = self.__createSquares()
        self.__dices = [Dice() for i in range(2)]
        self.__oxygen = 25
        self.playerInfos = [PlayerInfo(player) for player in players]
    
    def __createSquares(self):
        sf=SquareFactory()
        squares = []
        for i in range(1,4):
            squares.extend( sf.createSquares(i) )
        return squares

    def getSquares(self):
        return self.__squares
    def breathPlayer(self,playerNum):
        playerInfo = self.playerInfos[playerNum]
        self.__oxygen -= playerInfo.getSquareNum()
    def decideDirectionPlayer(self,playerNum):
        playerInfo = self.playerInfos[playerNum]
        playerInfo.decideDirection()
    def decideGetSquare(self,playerNum):
        playerInfo = self.playerInfos[playerNum]
        square = self.__squares[playerInfo.getPlace()]
        playerInfo.decideGetSquare(square)

    def forwordPlayer(self,playerNum):
        playerInfo = self.playerInfos[playerNum]
        diceNum=self.__getDiceNum() - playerInfo.getSquareNum()
        if playerInfo.isReverse():
            place = playerInfo.getPlace() - diceNum
        else:
            place = playerInfo.getPlace() + diceNum
        if place >= len(self.__squares):
            playerInfo.changeDirection()
            place =  2 * len(self.__squares) -  place - 2
        self.__squares[playerInfo.getPlace()].movePlayer()
        self.__setPlace(playerInfo,place)
    
    def printBoard(self):
        print("oxygen: "+ str(self.__oxygen))
        print( [ square.printBoard() for square in self.__squares])

        
    def __setPlace(self,playerInfo,place):
        if place < 0:
            playerInfo.setPlace(-1)
        else:
            while not self.__squares[place].isEmpty():
                if playerInfo.isReverse():
                    place-=1
                else:
                    place+=1
            playerInfo.setPlace(place)
            self.__squares[place].setPlayer(playerInfo.getPlayer())
    
    def __getDiceNum(self):
        return sum(map(lambda x:x.shake(),self.__dices))
    
