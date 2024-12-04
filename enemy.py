import pygame
from constants import Constatns as K

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = self.load_and_scale_image(K.CONAN_SWING_LEFT)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = 3  # Example health value

    def load_and_scale_image(self, path):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, K.PLAYER_DIMENSIONS)

    def update(self):
        # Add enemy movement logic here if needed
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove the enemy from the game