from smart_vac import SmartVac
from room_builder import Room

class Room_Mapper:
    def __init__(self, vac, room):
        self.room = room
        self.vac = vac
        self.visited_spaces = {}
