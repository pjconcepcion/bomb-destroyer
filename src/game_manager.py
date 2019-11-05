import math, random, time
from .game_environment import Enemy
from .screen import Text

class GameManager:
    def __init__(self, screen, player, game_environment):
        self._screen = screen
        self._player = player
        self._game_environment = game_environment
        self._scoreText = Text(const_val = 'Score', init_val = '0', color = (255,255,255), size = 20)
        self._lifeText = Text(const_val = 'Life',init_val = self._player.get_life(), color = (255,255,255), top = 30 , size = 20)

        self.set_player_bound()
        self._player.set_location(y = self._screen.get_height()/2, x = math.ceil(self._game_environment.get_ground().get_width() / 2))
        self._enemy_list = {}
        self._enemyCtr = 1
        self._totalEnemy = 1
        self._maxSpawn = 8
        self._score = 0
        self._is_game_over = False
        self._increase_speed = False

    def blit_all(self):
        self._screen.blit(self._screen.get_background(), self._screen.get_background_location())
        self.blit_enemy()
        self._screen.blit(self._game_environment.get_ground().get_floor(), self._game_environment.get_ground().get_location())
        self._screen.blit(self._player.get_player(), self._player.get_location())
        self._screen.blit(self._scoreText.get_text_surf(), self._scoreText.get_location())
        self._screen.blit(self._lifeText.get_text_surf(), self._lifeText.get_location())

        if (self._is_game_over == True):
            top = self._screen.get_height() // 2 - self._game_environment.get_ground().get_height()
            self._gameOverText = Text(const_val = 'Game Over', color = (255,0,0), top = top - 20)
            self._gameOverText.set_text(f'{self._score}')
            self._gameOverText.set_size(25)
            
            self._restartText = Text(const_val = 'ESC - Quit, R - Restart', separator = '', color = (255,0,0), top = top + 20)
            self._restartText.set_size(20)
            self._screen.blit(self._gameOverText.get_text_surf(), self._gameOverText.get_location())
            self._screen.blit(self._restartText.get_text_surf(), self._restartText.get_location())

    def blit_enemy(self):
        for enemy in self._enemy_list.values():
            self._screen.blit(enemy.get_enemy(), enemy.get_location())

    def set_player_bound(self):
        right = self._screen.get_width() - 20
        bottom = self._screen.get_height() - self._game_environment.get_ground().get_height() - 20
        self._player.set_bounds(right = right, bottom = bottom)

    def check_collision(self):
        if (self._player.get_rect().colliderect(self._game_environment.get_ground().get_rect())):
            self._player.set_grounded(True)

        if(len(self._enemy_list) > 0):
            for key in list(self._enemy_list):
                enemy = self._enemy_list
                if (self._player.get_rect().colliderect(enemy[key].get_rect()) and enemy[key].get_is_destroy() == False):
                    if(self._player.get_grounded() == False):
                        self._enemyCtr -= 1
                        self._score += 10
                        self._scoreText.set_text(self._score)
                        if (self._totalEnemy != self._maxSpawn):
                            self._totalEnemy += 1
                    else:
                        self._player.on_damage()
                        life = self._player.get_life()

                        if (life == 0):
                            self._is_game_over = True
                        self._lifeText.set_text(life)

                    enemy[key].set_is_destroy(True)
                    del self._enemy_list[key]

                elif (enemy[key].get_rect().colliderect(self._game_environment.get_ground().get_rect())):
                    x = random.randint(0,self._screen.get_width())
                    enemy[key].set_location(x = x, y = 0)

    def spawn_enemy(self):
        x = random.randint(0,self._screen.get_width())
        new_enemy = Enemy(left = x, name=f"Enemy-0{self._enemyCtr}")
        new_enemy.set_bound(self._screen.get_height() - self._game_environment.get_ground().get_height())

        hasNoCollision = True
        while (hasNoCollision):
            for enemy in self._enemy_list.values():
                if(enemy.get_init_rect().colliderect(new_enemy.get_rect())):
                    x = random.randint(0,self._screen.get_width())
                    new_enemy.relocate(left = x)
                    hasNoCollision = False

            if (hasNoCollision):
                break

        self._enemy_list.update({self._enemyCtr: new_enemy})
        self._enemyCtr += 1

    def move_enemy(self):
        for enemy in self._enemy_list.values():
            enemy.move()

    def run_background(self):
        if(not self._is_game_over):
            self._player.auto_move()
            self.check_collision()
            if (len(self._enemy_list) < self._totalEnemy):
                self.spawn_enemy()
            self.move_enemy()

    def is_game_over(self):
        return self.is_game_over