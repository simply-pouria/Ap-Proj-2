from random import randint

class Player:

    initial_coordination = {'red': 1, 'blue': 22}

    def __init__(self, color: str):

        self.traveled = 0
        self.coordination = Player.initial_coordination[color]
        self.color = color

    def move_forward(self, distance: int):
        self.traveled += distance
        self.coordination += distance

    def move_backward(self, distance: int):
        self.traveled -= distance
        self.coordination -= distance
    
    def update_gui(self):
        pass



def game_loop():

    # player 1 turn
    dice_1 = randint(1, 6)












