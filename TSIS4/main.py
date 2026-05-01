import pygame
import sys
import db
import random
import json
from game import Snake, Food, Obstacle, PowerUp # Импорты сверху

def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {"snake_color": [50, 200, 50], "sound": True, "grid": False}

def save_settings(data):
    with open("settings.json", "w") as f:
        json.dump(data, f)

current_settings = load_settings()
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE, BLACK, GRAY = (255, 255, 255), (0, 0, 0), (200, 200, 200)
COLORS = {"Green": (50, 200, 50), "Blue": (50, 50, 200), "Purple": (150, 50, 200), "Pink": (255, 105, 180)}
color_names = list(COLORS.keys())
current_color_idx = 0

STATE_MENU, STATE_GAME, STATE_GAMEOVER = "MENU", "GAME", "GAMEOVER"
STATE_LEADERBOARD, STATE_SETTINGS = "LEADERBOARD", "SETTINGS"
current_state = STATE_MENU

user_name = ""
personal_best = 0
db.init_db()

def draw_text(text, size, x, y, color=BLACK):
    font = pygame.font.SysFont("arial", size)
    surf = font.render(str(text), True, color)
    rect = surf.get_rect(center=(x, y))
    screen.blit(surf, rect)

def reset_game(name):
    snake = Snake(current_settings["snake_color"])
    food = Food(WIDTH, HEIGHT, False)
    poison = Food(WIDTH, HEIGHT, True)
    best = db.get_personal_best(name)
    return snake, food, poison, [], 0, 1, best, None, 0

# Инициализация переменных игры
snake, food, poison, walls, score, level, personal_best, power_up, effect_end_time = [None]*9

running = True
while running:
    screen.fill(WHITE)
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

        # Обработка событий в зависимости от экрана
        if current_state == STATE_MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: current_state = STATE_LEADERBOARD
                elif event.key == pygame.K_s: current_state = STATE_SETTINGS
                elif event.key == pygame.K_RETURN and len(user_name) > 0:
                    snake, food, poison, walls, score, level, personal_best, power_up, effect_end_time = reset_game(user_name)
                    current_state = STATE_GAME
                elif event.key == pygame.K_BACKSPACE: user_name = user_name[:-1]
                elif len(user_name) < 15 and event.unicode.isalnum(): user_name += event.unicode

        elif current_state == STATE_LEADERBOARD:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m: current_state = STATE_MENU

        elif current_state == STATE_SETTINGS:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g: current_settings["grid"] = not current_settings["grid"]
                elif event.key == pygame.K_s: current_settings["sound"] = not current_settings["sound"]
                elif event.key == pygame.K_c:
                    current_color_idx = (current_color_idx + 1) % len(color_names)
                    current_settings["snake_color"] = COLORS[color_names[current_color_idx]]
                elif event.key == pygame.K_m: save_settings(current_settings); current_state = STATE_MENU

        elif current_state == STATE_GAMEOVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake, food, poison, walls, score, level, personal_best, power_up, effect_end_time = reset_game(user_name)
                    current_state = STATE_GAME
                elif event.key == pygame.K_m: current_state = STATE_MENU

    # Отрисовка экранов
    if current_state == STATE_MENU:
        draw_text("SNAKE GAME", 50, WIDTH//2, 100)
        draw_text(f"Enter Name: {user_name}|", 24, WIDTH//2, 230)
        draw_text("Press ENTER to Play / L - Leaderboard / S - Settings", 16, WIDTH//2, 340)

    elif current_state == STATE_LEADERBOARD:
        draw_text("TOP 10 ALL-TIME", 30, WIDTH//2, 50, (255, 50, 0))
        top = db.get_top_10()
        for i, row in enumerate(top):
            draw_text(f"{i+1}. {row[0]} - {row[1]} (Lvl {row[2]})", 20, WIDTH//2, 100 + i*25)
        draw_text("Press M for Menu", 18, WIDTH//2, 370, GRAY)

    elif current_state == STATE_SETTINGS:
        draw_text("SETTINGS", 40, WIDTH//2, 50)
        draw_text(f"Grid: {'ON' if current_settings['grid'] else 'OFF'} (G)", 25, WIDTH//2, 150)
        draw_text(f"Sound: {'ON' if current_settings['sound'] else 'OFF'} (S)", 25, WIDTH//2, 200)
        draw_text("Snake Color (C):", 25, WIDTH//2 - 30, 250)
        pygame.draw.rect(screen, current_settings["snake_color"], (WIDTH//2 + 80, 240, 20, 20))
        draw_text("Press M to Menu", 18, WIDTH//2, 350, GRAY)

    elif current_state == STATE_GAME:
        if current_settings["grid"]:
            for x in range(0, WIDTH, 10): pygame.draw.line(screen, (230, 230, 230), (x, 0), (x, HEIGHT))
            for y in range(0, HEIGHT, 10): pygame.draw.line(screen, (230, 230, 230), (0, y), (WIDTH, y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != "d": snake.direction = "u"
        elif keys[pygame.K_DOWN] and snake.direction != "u": snake.direction = "d"
        elif keys[pygame.K_LEFT] and snake.direction != "r": snake.direction = "l"
        elif keys[pygame.K_RIGHT] and snake.direction != "l": snake.direction = "r"

        snake.move()
        head = snake.body[0]

        if snake.check_collision(WIDTH, HEIGHT, walls):
            db.save_result(user_name, score, level)
            current_state = STATE_GAMEOVER
            continue

        if head == food.pos:
            score += 1
            food.spawn(WIDTH, HEIGHT, walls, snake.body)
            if score % 5 == 0:
                level += 1; snake.speed += 2
                if level >= 3:
                    new_walls = Obstacle(snake.body + walls + [food.pos], WIDTH, HEIGHT, 3)
                    walls.extend(new_walls.blocks)
        else:
            snake.body.pop()

        if head == poison.pos:
            if snake.eat(is_poison=True): # Если вернул True - змея умерла
                db.save_result(user_name, score, level); current_state = STATE_GAMEOVER; continue
            poison.spawn(WIDTH, HEIGHT, walls, snake.body)

        if power_up is None and random.randint(1, 200) == 1:
            power_up = PowerUp(WIDTH, HEIGHT)
        
        if power_up:
            if power_up.is_expired(): power_up = None
            elif head == power_up.pos:
                effect_end_time = pygame.time.get_ticks() + 5000
                if power_up.type == "speed": snake.speed += 7
                elif power_up.type == "slow": snake.speed = max(5, snake.speed - 5)
                elif power_up.type == "shield": snake.shield = True
                power_up = None

        if effect_end_time > 0 and pygame.time.get_ticks() > effect_end_time:
            snake.speed = 10 + (level - 1) * 2
            effect_end_time = 0

        # Отрисовка игры
        for b in walls: pygame.draw.rect(screen, (100, 100, 100), (b[0], b[1], 9, 9))
        for s in snake.body: pygame.draw.rect(screen, snake.color, (s[0], s[1], 9, 9))
        if snake.shield: pygame.draw.rect(screen, (0, 255, 255), (head[0], head[1], 9, 9), 2)
        pygame.draw.rect(screen, food.color, (food.pos[0], food.pos[1], 9, 9))
        pygame.draw.rect(screen, poison.color, (poison.pos[0], poison.pos[1], 9, 9))
        if power_up: pygame.draw.rect(screen, power_up.color, (power_up.pos[0], power_up.pos[1], 9, 9))
        draw_text(f"Score: {score}  Level: {level}  Best: {personal_best}", 18, WIDTH//2, 20)
        clock.tick(snake.speed)

    elif current_state == STATE_GAMEOVER:
        draw_text("GAME OVER", 50, WIDTH//2, 100, (200, 0, 0))
        draw_text(f"Score: {score} | Level: {level}", 25, WIDTH//2, 200)
        draw_text("Press R to Restart / M for Menu", 18, WIDTH//2, 300)

    pygame.display.flip()