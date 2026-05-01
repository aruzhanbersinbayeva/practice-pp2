import pygame
import random
import sys
from snake import Snake

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Practice 11")

clock = pygame.time.Clock()

snake = Snake()

# ---------- FOOD ----------
food_pos = [random.randrange(1, 49)*10, random.randrange(1, 49)*10]
food_spawn_time = pygame.time.get_ticks()

food_value = random.choice([1,2,3,5])

# ---------- GAME VARIABLES ----------
score = 0
level = 1
speed = 10

font = pygame.font.SysFont("Arial", 25)
game_state = "play"

# ---------- FUNCTIONS ----------

def new_food():
    global food_pos, food_value, food_spawn_time

    while True:
        x = random.randrange(1, 49)*10
        y = random.randrange(1, 49)*10

        if [x,y] not in snake.body:
            food_pos = [x,y]
            break

    food_value = random.choice([1,2,3,5])
    food_spawn_time = pygame.time.get_ticks()


def check_collision():
    global score, level, speed

    # food collision
    if snake.body[0] == food_pos:

        score += food_value
        snake.grow()
        new_food()

        # level system
        if score // 3 + 1 > level:
            level += 1
            speed += 2


def check_wall():

    head = snake.body[0]

    if head[0] < 0 or head[0] > 490 or head[1] < 0 or head[1] > 490:
        return True

    return False


# ---------- GAME LOOP ----------
running = True

while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    snake.change_dir()
    snake.move()


    # ---------- FOOD TIMER (disappears) ----------
    if pygame.time.get_ticks() - food_spawn_time > 5000:
        new_food()


    # ---------- COLLISIONS ----------
    check_collision()

    if check_wall():
        print("Game Over")
        pygame.quit()
        sys.exit()


    # ---------- DRAW SNAKE ----------
    for block in snake.body:
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(block[0], block[1], 10, 10))


    # ---------- DRAW FOOD ----------
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # show food weight
    weight_text = font.render(str(food_value), True, (255,255,0))
    screen.blit(weight_text, (food_pos[0], food_pos[1]-20))


    # ---------- SCORE & LEVEL ----------
    score_text = font.render(f"Score: {score}", True, (255,255,255))
    level_text = font.render(f"Level: {level}", True, (255,255,255))

    screen.blit(score_text, (10,10))
    screen.blit(level_text, (10,40))


    pygame.display.update()
    clock.tick(speed)