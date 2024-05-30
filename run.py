import random

class Board:


    def __init__(self, size, ships_num):
        self.size = size
        self.board = [["[ ]" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        





def new_game():

    size = 5
    num_ships = 5
    print("." * 35)
    print("Welcome to Battleships Game!")
    print("." * 35)
    print("Board size: {size}. Number of ships: {ships} ")
