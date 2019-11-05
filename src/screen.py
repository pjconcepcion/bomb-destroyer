import pygame as pg

class Screen:
    def __init__(self):
        self._color = (255, 255, 255)
        self._size = self._width, self._height = 300, 300
        self._rect = pg.Rect(0,0, self._width, self._height)
        self._screen = pg.display.set_mode(self._size)
        self._screen.fill(self._color)

        self._background = pg.image.load('assets/sky.jpg')
        self._background_location = self._background_x, self._background_y = 0,0

        pg.display.set_caption('Bomb Destroyer')

    def get_screen(self):
        return self._screen

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_size(self):
        return self._size

    def get_color(self):
        return self._color
    
    def get_screen_rect(self):
        return self._screen.rect

    def get_background(self):
        return self._background

    def get_background_location(self):
        return self._background_location
    
    def get_scoreText_location(self):
        return self._scoreText_location

    def get_scoreText(self):
        return self._scoreText

    def blit(self, source, dest):
        self._screen.blit(source,dest)

    def set_scoreText(self, text):
        self._score += text
        self._scoreText = self._font.render(f'Score: {self._score}', True, (0,0,0))


class Text:

    def __init__(self, const_val = '', separator = ':', init_val = '', color = (0,0,0), left = 10, top = 10, size = 15):
        self._score = 0
        self._size = size
        self._font = pg.font.Font('assets/arial.ttf', self._size)
        self._const_val = const_val
        self._separator = separator
        self._init_val = init_val
        self._text = f'{self._const_val} {self._separator} {self._init_val}'
        self._color = color
        self._location = self._text_left, self._text_top = left, top
        self._textSurf = self._font.render(self._text, True, self._color)
        self._rect = self._textSurf.get_rect()
        self._rect.center = (left // 2, top // 2)

    def get_text_surf(self):
        return self._textSurf

    def get_text(self):
        return self._text

    def get_location(self):
        return self._location

    def get_rect(self):
        return self._rect

    def set_text(self, text):
        self._text = f'{self._const_val}: {text}'
        self._textSurf = self._font.render(self._text, True, self._color)

    def set_color(self, color):
        self._color = color

    def set_size(self, size):
        self._font = pg.font.Font('assets/arial.ttf', size)
        self._textSurf = self._font.render(self._text, True, self._color)