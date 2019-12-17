import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"""
    def __init__(self, ai_settings, screen):
        """"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien_resized.png')
        self.image = pygame.transform.flip(self.image, 0, 1)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)