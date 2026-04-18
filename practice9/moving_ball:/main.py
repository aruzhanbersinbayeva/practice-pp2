import pygame
import sys
from ball import Ball

def main():
    pygame.init()
    
    # Размеры из твоего задания
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    
    ball = Ball(WIDTH, HEIGHT)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    ball = Ball(WIDTH, HEIGHT) # Сброс
                
                # Управление стрелками
                elif event.key == pygame.K_UP:
                    ball.move("up")
                elif event.key == pygame.K_DOWN:
                    ball.move("down")
                elif event.key == pygame.K_LEFT:
                    ball.move("left")
                elif event.key == pygame.K_RIGHT:
                    ball.move("right")

        screen.fill((245, 245, 245)) # Светлый фон
        ball.draw(screen)            # Рисуем мяч
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()