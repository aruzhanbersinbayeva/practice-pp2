import pygame
import random
import sys

from player import Player
from coin import Coin

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

FPS = 60
clock = pygame.time.Clock()

# ---------- Game state ----------
game_state = "play"  # play / game_over

# ---------- Road ----------
road = pygame.image.load("racer/images/street.png")
road = pygame.transform.scale(road, (400, 600))

road_y1 = 0
road_y2 = -600
scroll_speed = 5

# ---------- Enemy ----------
enemy_img = pygame.image.load("racer/images/Enemy-2.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
enemy_rect = enemy_img.get_rect()
enemy_rect.center = (random.randint(80, 320), 0)
enemy_speed = 5

# ---------- Player ----------
player = Player()

# ---------- Coin ----------
coin = Coin()

font = pygame.font.SysFont("Arial", 30)

score = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------- Controls in Game Over ----------
        if game_state == "game_over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    score = 0
                    enemy_speed = 5

                    player.rect.center = (200, 500)
                    enemy_rect.center = (random.randint(80, 320), 0)
                    coin.reset()

                    game_state = "play"

                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    sys.exit()

    # ================= PLAY STATE =================
    if game_state == "play":

        # ---------- Road ----------
        road_y1 += scroll_speed
        road_y2 += scroll_speed

        if road_y1 >= 600:
            road_y1 = -600
        if road_y2 >= 600:
            road_y2 = -600

        screen.blit(road, (0, road_y1))
        screen.blit(road, (0, road_y2))

        # ---------- Player ----------
        player.move()
        screen.blit(player.image, player.rect)

        # ---------- Enemy ----------
        enemy_rect.move_ip(0, enemy_speed)

        if enemy_rect.top > 600:
            enemy_rect.center = (random.randint(80, 320), 0)

        screen.blit(enemy_img, enemy_rect)

        # ---------- Coin ----------
        coin.move()
        screen.blit(coin.image, coin.rect)

        weight_text = font.render(str(coin.value), True, (255, 255, 0))
        screen.blit(weight_text, (coin.rect.x, coin.rect.y - 25))

        # ---------- Collect coin ----------
        if player.rect.colliderect(coin.rect):
            score += coin.value
            coin.reset()

            if score % 10 == 0:
                enemy_speed += 1

        # ---------- Crash ----------
        if player.rect.colliderect(enemy_rect):
            game_state = "game_over"

        # ---------- Score ----------
        score_text = font.render(f"Coins: {score}", True, (255, 255, 255))
        screen.blit(score_text, (240, 20))

    # ================= GAME OVER =================
    elif game_state == "game_over":

        screen.fill((0, 0, 0))

        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))
        quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
        score_text = font.render(f"Score: {score}", True, (255, 255, 0))

        screen.blit(game_over_text, (100, 180))
        screen.blit(score_text, (120, 240))
        screen.blit(restart_text, (70, 320))
        screen.blit(quit_text, (90, 370))

    pygame.display.update()
    clock.tick(FPS)