import pygame

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 25
        self.step = 20
        self.x = screen_width // 2
        self.y = screen_height // 2

    def move(self, direction):
        if direction == "up" and self.y - self.step >= self.radius:
            self.y -= self.step
        elif direction == "down" and self.y + self.step <= self.screen_height - self.radius:
            self.y += self.step
        elif direction == "left" and self.x - self.step >= self.radius:
            self.x -= self.step
        elif direction == "right" and self.x + self.step <= self.screen_width - self.radius:
            self.x += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, (220, 40, 40), (self.x, self.y), self.radius)

    def get_position(self):
        return (self.x, self.y)