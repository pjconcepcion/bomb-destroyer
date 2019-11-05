import pygame as pg

class GameEnvironment:

    def __init__(self, width = 0, height = 0):
        self._size = self._width, self._height = width, height
        self._ground = Floor(top = height - 20, width = width, height = 20, color = (87, 240, 31), img = 'assets/brick.png')

    def get_ground(self):
        return self._ground

class Floor:
    def __init__(self, left = 0, top = 0, width = 0, height = 0, color = (0,0,0), img = None):
        self._location = self._left, self._top = left, top
        self._size = self._width, self._height = width, height
        self._rect = pg.Rect(self._location, self._size) 
        self._color = color
        self._floor = pg.Surface(self._size) if img == None else pg.image.load(img)

    def get_rect(self):
        return self._rect

    def get_floor(self):
        return self._floor

    def get_location(self):
        return self._location

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_size(self):
        return self._size

class Enemy:
    def __init__(self, left = 0, top = 0, width = 0, height = 0, name = "Enemy"):
        self._size = self._width, self._height = 30, 30
        self._location = self._left, self._top = left, top
        self._rect = pg.Rect(self._location, self._size)
        self._init_rect = self._rect
        self._enemy = pg.Surface(self._size)
        self._enemy = pg.image.load('assets/tnt.jpg')
        self._enemy = pg.transform.scale(self._enemy, self._size)
        self._speed = 10
        self._is_destroy = False
        self._name = name

    def get_rect(self):
        return self._rect

    def get_init_rect(self):
        return self._init_rect

    def get_enemy(self):
        return self._enemy

    def get_location(self):
        return self._location

    def get_is_destroy(self):
        return self._is_destroy

    def get_name(self):
        return self._name

    def set_rect(self, left = 0, top = 0):
        self._rect = pg.Rect((left, top), self._size)

    def set_location(self, x = 0, y = 0):
        self._location = self._left, self._top = x, y

    def set_bound(self, y):
        self._bound = y

    def set_is_destroy(self, is_destroy):
        self._is_destroy = is_destroy

    def increase_speed(self):
        self._speed += 2

    def relocate(self, left = 0, top = 0):
        self.set_location(left,top)
        self.set_rect(left,top)

    def move(self):
        if (self._top > self._bound):
            self._top = 0

        self._top += self._speed/2
        self.set_location(self._left, self._top)
        self.set_rect(self._left, self._top)