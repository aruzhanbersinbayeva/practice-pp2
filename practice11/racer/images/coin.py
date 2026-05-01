import pygame
import random

class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("racer/images/coin.png")
        self.image = pygame.transform.scale(self.image,(30,30))

        self.rect = self.image.get_rect()

        self.reset()

    def reset(self):

        self.rect.center=(
            random.randint(80,320),
            random.randint(-300,-50)
        )

        # Different weights
        self.value=random.choice([1,3,5])

    def move(self):

        self.rect.move_ip(0,5)

        if self.rect.top>600:
            self.reset()