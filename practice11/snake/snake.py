import pygame

class Snake:

    def __init__(self):

        # starting body
        self.body = [[100,100],[90,100],[80,100]]

        self.direction = "RIGHT"
        self.change_to = self.direction

    def change_dir(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.direction != "RIGHT":
            self.change_to = "LEFT"

        if keys[pygame.K_RIGHT] and self.direction != "LEFT":
            self.change_to = "RIGHT"

        if keys[pygame.K_UP] and self.direction != "DOWN":
            self.change_to = "UP"

        if keys[pygame.K_DOWN] and self.direction != "UP":
            self.change_to = "DOWN"


    def move(self):

        self.direction = self.change_to

        head = self.body[0].copy()

        if self.direction == "RIGHT":
            head[0] += 10

        if self.direction == "LEFT":
            head[0] -= 10

        if self.direction == "UP":
            head[1] -= 10

        if self.direction == "DOWN":
            head[1] += 10

        self.body.insert(0, head)
        self.body.pop()
    def check_collision(self, width, height):

        head = self.body[0]

        # удар в стену
        if head[0] < 0 or head[0] >= width:
            return True
        if head[1] < 0 or head[1] >= height:
            return True

        # удар в себя
        if head in self.body[1:]:
            return True

        return False

    def grow(self):
        self.body.append(self.body[-1])