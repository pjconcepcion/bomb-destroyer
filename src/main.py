import pygame as pg
from .screen import Screen
from .player import Player
from .game_environment import GameEnvironment
from .game_manager import GameManager

class Main:
    FPS = 30

    def __init__(self):
        self.running = True
        pg.init()
        print("Game initializing...")
    
    def on_event(self, event):
        if (event.type == pg.QUIT):
            self.running = False
        if (event.type == pg.KEYDOWN):
            self.player.set_move(event.key, True)
        if (event.type == pg.KEYUP):
            self.player.set_move(event.key, False)
        if (self.game_manager.is_game_over() and event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE):
                self.running = False
            elif (event.key == pg.K_r):
                self.start()

    def on_loop(self):
        self.game_manager.run_background()
        self.player.moving()

    def on_render(self):
        self.game_manager.blit_all()
        pg.display.flip()

    def on_cleanup(self):
        pg.quit()

    def initialize(self):
        self.screen = Screen()
        self.player = Player()
        self.environment = GameEnvironment(self.screen.get_width(), self.screen.get_height())
        self.game_manager = GameManager(self.screen, self. player, self.environment)

    def start(self):
        print("Game start...")
        self.initialize()

        while (self.running):
            for event in pg.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

            pg.time.delay(self.FPS)

        self.on_cleanup()