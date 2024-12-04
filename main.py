import pygame
import sys 
from constants import Constatns as K
from player import Player

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((K.SCREEN_WIDTH,
                                  K.SCREEN_LENGTH))
pygame.display.set_caption("Conan the Barbarian")

background = pygame.image.load(K.LEVEL_1).convert()
background = pygame.transform.scale(background, (K.SCREEN_WIDTH, K.SCREEN_LENGTH))

clock = pygame.time.Clock()

# Sprites

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

def run():
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.blit(background, (0, 0))  # Draw the background

        all_sprites.draw(screen)

        pygame.display.flip()

        clock.tick(K.FPS)

if __name__ == '__main__':
    run()