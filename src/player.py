import pygame as pg, time

class Player:
    def __init__(self):
        self._size = self._width, self._height = 30,20
        self._location = self._x, self._y = 10,10
        self._rect = pg.Rect(self._location, self._size)
        self._player = pg.Surface(self._size)
        self._player = pg.image.load('assets/metal.png')
        self._player = pg.transform.scale(self._player, self._size)
        self._keys = {'RIGHT': False, 'LEFT': False, 'UP': False, 'DOWN': False}
        self._is_grounded = False
        self._life = 3
        self._is_dead = False
        self._jump_time = time.time()
        self._jump_rate = 1.5

    def get_rect(self):
        return self._rect

    def get_player(self):
        return self._player

    def get_location(self):
        return self._location

    def get_bounds(self):
        return self._bounds

    def get_grounded(self):
        return self._is_grounded

    def get_life(self):
        return self._life

    def set_rect(self, x, y):
        self._rect = pg.Rect((x, y), self._size)

    def set_move(self, key, pressed):
        if (key == pg.K_w):
            self._keys['UP'] = True if pressed else False
        if (key == pg.K_a):
            self._keys['LEFT'] = True if pressed else False
        if (key == pg.K_s):
            self._keys['DOWN'] = True if pressed else False
        if (key == pg.K_d):
            self._keys['RIGHT'] = True if pressed else False

    def set_location(self, x, y):
        self.set_rect(x,y)
        self._location = self._x, self._y = x, y

    def set_bounds(self, left = 0, right = 0, top = 0, bottom = 0):
        self._bounds = self._bound_top, self._bound_left, self._bound_right, self._bound_bottom = top, left, right, bottom

    def set_grounded(self, is_grounded):
        self._is_grounded = is_grounded

    def on_damage(self):
        self._life -= 1
        if (self._life == 0):
            self._is_dead = True

    def moving(self):
        if (self._is_dead == False):
            if (self._keys['UP'] == True and self._y >= self._bound_top and self._is_grounded == True):
                if (time.time() > self._jump_time):
                    self._jump_time = time.time() + self._jump_rate
                    self._y -= 25
                    self.set_grounded(False)
            if (self._keys['DOWN'] == True and self._y <= self._bound_bottom):
                self._y += 2
            if (self._keys['LEFT'] == True and self._x >= self._bound_left):
                self._x -= 5
            if (self._keys['RIGHT'] == True and self._x <= self._bound_right):
                self._x += 5
            self.set_location(self._x, self._y)
            return False
        return True

    def auto_move(self, x = 1, y = 1):
        if (self._y <= self._bound_bottom):
            self._y += 2