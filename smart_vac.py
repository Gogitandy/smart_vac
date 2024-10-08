from random import randint
from room_builder import Room

class SmartVac:
    def __init__ (self, room):
        #initialize vac
        self.room = room
        self.map = {}
        self.converted_map = []
        self.left_sensor = 0
        self.right_sensor = 0
        self.front_sensor = 0
        self.back_sensor = 0
        self.direction = 0
        #set vac starting position in random open cell
        while True:
            y_p = randint(0, self.room.nrows -1)
            x_p = randint(0, self.room.ncols -1)
            if self.room.layout[y_p][x_p]:
                self.position = (x_p, y_p)
                break
        return
