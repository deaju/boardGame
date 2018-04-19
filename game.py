# coding:utf-8
from player import Player
from board import Board

players = [Player(0), Player(1)]
board = Board(players)


def turn(num):
    board.breathPlayer(num)
    board.printBoard()
    print('direction')
    board.decideDirectionPlayer(num)
    board.forwordPlayer(num)
    board.printBoard()
    print('Do you want to get?')
    board.decideGetSquare(num)
    if board.playerInfos[num].isGoal():
        print('GOAL!point :' + str(board.playerInfos[num].calcPoint()))
    board.printBoard()