import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

# ── Screen ─────────────────────────────
W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racer")

# ── Colors ─────────────────────────────
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
GRAY  = (90, 90, 90)
BLUE  = (30, 90, 210)
RED   = (210, 40, 40)
YELLOW = (255, 215, 0)

font = pygame.font.SysFont("Arial", 22, True)
big  = pygame.font.SysFont("Arial", 48, True)

# ── Road limits ────────────────────────
LEFT, RIGHT = 60, 340


# ── Road ───────────────────────────────
class Road:
    def __init__(self):
        self.off = 0
        self.speed = 5

    def update(self):
        self.off = (self.off + self.speed) % 80

    def draw(self, s):
        s.fill(GREEN)
        pygame.draw.rect(s, GRAY, (LEFT, 0, RIGHT-LEFT, H))
        pygame.draw.rect(s, WHITE, (LEFT-4, 0, 4, H))
        pygame.draw.rect(s, WHITE, (RIGHT, 0, 4, H))

        for x in (LEFT+90, LEFT+180):
            y = self.off - 80
            while y < H:
                pygame.draw.rect(s, WHITE, (x, y, 3, 40))
                y += 80


# ── Player ─────────────────────────────
class Player:
    def __init__(self):
        self.x, self.y = 180, 500
        self.w, self.h = 38, 68
        self.spd = 5

    def move(self, k):
        if k[pygame.K_LEFT]:  self.x -= self.spd
        if k[pygame.K_RIGHT]: self.x += self.spd
        if k[pygame.K_UP]:    self.y -= self.spd
        if k[pygame.K_DOWN]:  self.y += self.spd

    def draw(self, s):
        x, y = self.x, self.y

        pygame.draw.rect(s, BLUE, (x, y, self.w, self.h), border_radius=8)
        pygame.draw.rect(s, (170, 220, 255), (x+5, y+10, self.w-10, 18))
        pygame.draw.rect(s, (170, 220, 255), (x+5, y+self.h-28, self.w-10, 14))
        pygame.draw.circle(s, WHITE, (x+7, y+self.h-5), 3)
        pygame.draw.circle(s, WHITE, (x+self.w-7, y+self.h-5), 3)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)


# ── Enemy (simple but same design) ─────────────────────
class Enemy:
    def __init__(self, speed):
        lane = random.randint(0, 2)
        self.x = LEFT + lane * 90
        self.y = -70
        self.spd = speed

    def update(self):
        self.y += self.spd

    def draw(self, s):
        x, y = self.x, self.y

        pygame.draw.rect(s, RED, (x, y, 38, 68), border_radius=8)
        pygame.draw.rect(s, (200, 220, 255), (x+5, y+10, 28, 16))
        pygame.draw.circle(s, WHITE, (x+7, y+63), 3)
        pygame.draw.circle(s, WHITE, (x+31, y+63), 3)

    def rect(self):
        return pygame.Rect(self.x, self.y, 38, 68)


# ── Coin ───────────────────────────────
class Coin:
    def __init__(self, speed):
        self.x = random.randint(LEFT, RIGHT)
        self.y = -20
        self.spd = speed

    def update(self):
        self.y += self.spd

    def draw(self, s):
        pygame.draw.circle(s, YELLOW, (self.x, self.y), 10)

    def rect(self):
        return pygame.Rect(self.x-10, self.y-10, 20, 20)


# ── HUD ────────────────────────────────
def hud(s, score, coins):
    t = font.render(f"Score: {score}  Coins: {coins}", True, WHITE)
    s.blit(t, (10, 10))


# ── Game Over ──────────────────────────
def game_over(s, score, coins):
    s.blit(big.render("GAME OVER", True, RED), (90, 200))
    s.blit(font.render(f"Score: {score}", True, WHITE), (120, 260))
    s.blit(font.render("R - restart   Q - quit", True, WHITE), (80, 300))


# ── Main ───────────────────────────────
def main():
    road = Road()
    player = Player()

    enemies = []
    coins = []

    score = 0
    coin_count = 0
    over = False

    while True:
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if e.type == pygame.KEYDOWN and over:
                if e.key == pygame.K_r:
                    main()
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()

        if not over:
            player.move(keys)
            road.update()

            if random.randint(1, 70) == 1:
                enemies.append(Enemy(5))

            if random.randint(1, 120) == 1:
                coins.append(Coin(5))

            # enemies
            for e in enemies[:]:
                e.update()
                if e.rect().colliderect(player.rect()):
                    over = True
                if e.y > H:
                    enemies.remove(e)
                    score += 1

            # coins
            for c in coins[:]:
                c.update()
                if c.rect().colliderect(player.rect()):
                    coins.remove(c)
                    coin_count += 1

        # draw
        road.draw(screen)

        for e in enemies:
            e.draw(screen)

        for c in coins:
            c.draw(screen)

        player.draw(screen)

        hud(screen, score, coin_count)

        if over:
            game_over(screen, score, coin_count)

        pygame.display.flip()


if __name__ == "__main__":
    main()