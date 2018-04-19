# coding:utf-8

class Player():
    def __init__(self,id):
        self.id = id
    def printBoard(self):
        return 'player '+str(self.id)
    def decideGetSquare(self):
        decide=int(input())
        return decide > 0

    def decideDirection(self):
        decide=int(input())
        return decide > 0