import pygame
from constants import Constatns as K

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load and resize images to PLAYER_DIMENSIONS
        self.image_right = pygame.transform.scale(pygame.image.load(K.CONAN_RIGHT).convert_alpha(), K.PLAYER_DIMENSIONS)
        self.image_left = pygame.transform.scale(pygame.image.load(K.CONAN_LEFT).convert_alpha(), K.PLAYER_DIMENSIONS)
        self.image_right_swing = pygame.transform.scale(pygame.image.load(K.CONAN_SWING_RIGHT).convert_alpha(), K.PLAYER_DIMENSIONS)
        self.image_left_swing = pygame.transform.scale(pygame.image.load(K.CONAN_SWING_LEFT).convert_alpha(), K.PLAYER_DIMENSIONS)
        self.image_flex = pygame.transform.scale(pygame.image.load(K.CONAN_FLEX).convert_alpha(), K.PLAYER_DIMENSIONS)

        # Player Attributes
        self.image = self.image_right  # face right first
        self.rect = self.image.get_rect()
        self.rect.center = (K.SCREEN_WIDTH // 2, K.SCREEN_LENGTH // 2)
        self.speed = 5  # base speed
        self.jump_power = 15  # base jump
        self.gravity = 1
        self.velocity_y = 0
        self.is_jumping = False

        # Sounds
        self.flex_sound = pygame.mixer.Sound(K.CONAN_FLEX_SOUND)

        # Animation state
        self.is_swinging = False
        self.swing_index = 0

        # Attack attributes
        self.attack_damage = 1
        self.attacking = False

        # Direction state
        self.facing_right = True

        # Timer for swing animation
        self.swing_timer = 0
        self.swing_duration = 8  

    def update(self):
        # Tracking key presses here
        keys = pygame.key.get_pressed()

        # Movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.image_left
            self.facing_right = False

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.image_right
            self.facing_right = True

        if keys[pygame.K_f]:
            self.image = self.image_flex
            self.flex_sound.play()

        if keys[pygame.K_s] and not self.is_swinging:
            print("Swinging initiated")
            self.is_swinging = True
            self.swing_index = 0
            self.attacking = True
            self.swing_timer = self.swing_duration

        # Jumping
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_power

        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

        # Check if landed
        if self.rect.bottom >= K.SCREEN_LENGTH:
            self.rect.bottom = K.SCREEN_LENGTH
            self.is_jumping = False
            self.velocity_y = 0

        # Handle swinging animation
        if self.is_swinging:
            self.animate_swing()

    def animate_swing(self):
        if self.swing_timer > 0:
            self.swing_timer -= 1
            if self.facing_right:
                self.image = self.image_right_swing
            else:
                self.image = self.image_left_swing
        else:
            self.is_swinging = False
            self.attacking = False
            self.image = self.image_right if self.facing_right else self.image_left  # Reset to default image after swinging