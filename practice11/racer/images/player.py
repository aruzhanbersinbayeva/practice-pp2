import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("racer/images/player.png")
        self.image = pygame.transform.scale(self.image,(50,100))

        self.rect = self.image.get_rect()

        self.rect.center=(200,520)

    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)

        if pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        # boundaries of road
        if self.rect.left < 65:
            self.rect.left = 65

        if self.rect.right > 335:
            self.rect.right = 335