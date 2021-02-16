import pygame
from sprite import Sprite
from pygame.transform import scale

class Player(Sprite):
    def __init__(self, game):
        super().__init__(game)
        self.image = pygame.image.load("res/player.png")
        self.image = scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 70

        

    def update(self, event):
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        speed = 1 / float(dt)

        if (event.player_left):
            self.rect.x -= speed

        if (event.player_right):
            self.rect.x += speed

        if (event.player_up):
            self.rect.y -= speed

        if (event.player_down):
            self.rect.y += speed


