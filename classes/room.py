import json
from utils.helpers import format_coin


class Room:
    rooms = []

    def __init__(self, id, price, capacity, available=True):
        self.id = id
        self.price = price
        self.capacity = capacity
        self.available = available
        self.rooms.append(self)
    
    def set_as_unavailable(self):
        self.available = False
    
    def set_as_available(self):
        self.available = True

    @staticmethod
    def load_rooms():
        print('Loading rooms...')
        rooms = open('data/rooms.json')
        rooms = json.load(rooms)
        for room in rooms:
            Room(room['id'], room['price'], room['capacity'])
    
    @classmethod
    def show_rooms(cls):
        print('  id  |  price  |  capacity(person)')
        for room in cls.rooms:
            if room.available:
                formatted_price = format_coin(str(room.price))
                print(f'  {room.id}  -  {formatted_price}  -  {room.capacity} ')
