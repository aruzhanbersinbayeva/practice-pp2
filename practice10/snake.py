import pygame
import sys
import random

pygame.init()
clock=pygame.time.Clock()

BLACK    = (0,   0,   0  )
WHITE    = (255, 255, 255)
DKGREEN  = (0,   140, 0  )
GREEN    = (50,  200, 50 )
RED      = (220, 40,  40 )
GRAY     = (30,  30,  30 )
LT_GRAY  = (60,  60,  60 )

UP=(0,-1)
DOWN=(0,1)
LEFT=(-1,0)
RIGHT=(1,0)
hud_h=50
col,row=30,25
cel=20
screen_w=col*cel
screen_h=row*cel + hud_h

screen=pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("Snake")
font=pygame.font.SysFont("Arial",22,bold=True)



def random_apple(apple):
    free=[]
    for c in range(1,col-1):
        for r in range(1,row-1):
            if (c,r) not in apple:
                free.append((c,r))
    return random.choice(free)

class Snake():
    def __init__(self):
        sx,sy=col//2,row//2
        self.body=[(sx,sy), (sx-1,sy), (sx-2,sy)]
        self.direction= RIGHT
        self.queued= RIGHT
        self.grow= False


    def queued_direction(self,new_dir):
        self.queued=new_dir


    def move(self):
        self.direction= self.queued
        hx,hy=self.body[0]
        new_head=(hx+self.direction[0],hy+self.direction[1])
        self.body.insert(0,new_head)
        if self.grow:
            self.grow=False
        else:
            self.body.pop()


    def eat(self):
        self.grow=True

    def hit_wall(self):
        hx,hy=self.body[0]
        if hx<0 or hx>=col:
            return True
        if hy<0 or hy>=row:
            return True
        return False
    def hit_self(self):
        return self.body[0] in self.body[1:]
    
    def draw(self, surface):
        for i, (c, r) in enumerate(self.body):
            x = c * cel
            y = r * cel + hud_h   # ← тут была ошибка!

            if i == 0:
                color = DKGREEN
            else:
                color = GREEN

            pygame.draw.rect(surface, color, (x, y, cel, cel))


    def cells(self):
        return set(self.body)

class Food():
    def __init__(self,apple):
        self.pos=random_apple(apple)
    def draw(self,surface):
        c,r=self.pos
        x = c * cel + cel // 2
        y = r * cel + cel // 2 + hud_h

        pygame.draw.circle(surface, RED, (x, y), cel // 2)

def draw_game_over(surface, score):
    text1 = font.render("GAME OVER", True, WHITE)
    text2 = font.render(f"Score: {score}", True, WHITE)
    text3 = font.render("R - restart   Q - quit", True, WHITE)

    surface.blit(text1, (screen_w//2 - text1.get_width()//2, screen_h//2 - 40))
    surface.blit(text2, (screen_w//2 - text2.get_width()//2, screen_h//2))
    surface.blit(text3, (screen_w//2 - text3.get_width()//2, screen_h//2 + 40))

def draw_hud(surface, score, level):
    pygame.draw.rect(surface, GRAY, (0, 0, screen_w, hud_h))

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    surface.blit(text, (10, 10))   

def draw_border(surface):
    pygame.draw.rect(surface, WHITE, (0, hud_h, screen_w, cel * row), 2)


def main():
    snake=Snake()
    food=Food(snake.cells())
    score             = 0
    level             = 1
    total_foods_eaten = 0 
    game_over = False
    while True:
        clock.tick(8)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                else:
                    if event.key == pygame.K_UP:
                        snake.queued_direction(UP)
                    if event.key == pygame.K_DOWN:
                        snake.queued_direction(DOWN)
                    if event.key == pygame.K_LEFT:
                        snake.queued_direction(LEFT)
                    if event.key == pygame.K_RIGHT:
                        snake.queued_direction(RIGHT)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            snake.move()

            if snake.hit_wall() or snake.hit_self():
                game_over = True

            if snake.body[0] == food.pos:
                snake.eat()
                score += 10
                food = Food(snake.cells())

        screen.fill(BLACK)
        draw_hud(screen, score, level)
        draw_border(screen)
        food.draw(screen)
        snake.draw(screen)

        if game_over:
            draw_game_over(screen, score)
        pygame.display.flip()

if __name__ == "__main__":
    main()

