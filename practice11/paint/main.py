import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Practice 11")

clock = pygame.time.Clock()

# ---------- COLORS ----------
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

current_color = BLACK

# ---------- MODES ----------
mode = "pen"  # pen, rect, circle, eraser, square, tri_right, tri_eq, rhombus

start_pos = None

screen.fill(WHITE)


# ---------- FUNCTIONS ----------

def draw_square(pos1, pos2):
    size = min(abs(pos2[0]-pos1[0]), abs(pos2[1]-pos1[1]))
    rect = pygame.Rect(pos1[0], pos1[1], size, size)
    pygame.draw.rect(screen, current_color, rect, 2)


def draw_right_triangle(p1, p2):
    pygame.draw.polygon(screen, current_color, [
        p1,
        (p1[0], p2[1]),
        p2
    ], 2)


def draw_equilateral_triangle(p1, p2):

    base = abs(p2[0]-p1[0])
    height = int(base * (3**0.5)/2)

    p3 = ((p1[0]+p2[0])//2, p1[1]-height)

    pygame.draw.polygon(screen, current_color, [p1,p2,p3], 2)


def draw_rhombus(p1,p2):

    center_x = (p1[0]+p2[0])//2
    center_y = (p1[1]+p2[1])//2

    dx = abs(p2[0]-p1[0])//2
    dy = abs(p2[1]-p1[1])//2

    points = [
        (center_x, center_y-dy),
        (center_x+dx, center_y),
        (center_x, center_y+dy),
        (center_x-dx, center_y)
    ]

    pygame.draw.polygon(screen, current_color, points, 2)


# ---------- LOOP ----------
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # ---------- KEYBOARD MODE SWITCH ----------
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                mode = "pen"

            if event.key == pygame.K_2:
                mode = "rect"

            if event.key == pygame.K_3:
                mode = "circle"

            if event.key == pygame.K_4:
                mode = "eraser"

            if event.key == pygame.K_5:
                mode = "square"

            if event.key == pygame.K_6:
                mode = "tri_right"

            if event.key == pygame.K_7:
                mode = "tri_eq"

            if event.key == pygame.K_8:
                mode = "rhombus"

            # colors
            if event.key == pygame.K_r:
                current_color = RED

            if event.key == pygame.K_g:
                current_color = GREEN

            if event.key == pygame.K_b:
                current_color = BLUE

            if event.key == pygame.K_y:
                current_color = YELLOW


        # ---------- MOUSE ----------
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos


        if event.type == pygame.MOUSEBUTTONUP:

            end_pos = event.pos

            # rectangle
            if mode == "rect":
                pygame.draw.rect(screen, current_color,
                                 pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])), 2)

            # circle
            if mode == "circle":
                radius = int(math.dist(start_pos, end_pos))
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

            # square
            if mode == "square":
                draw_square(start_pos, end_pos)

            # right triangle
            if mode == "tri_right":
                draw_right_triangle(start_pos, end_pos)

            # equilateral triangle
            if mode == "tri_eq":
                draw_equilateral_triangle(start_pos, end_pos)

            # rhombus
            if mode == "rhombus":
                draw_rhombus(start_pos, end_pos)


    # ---------- PEN + ERASER ----------
    if pygame.mouse.get_pressed()[0]:

        x,y = pygame.mouse.get_pos()

        if mode == "pen":
            pygame.draw.circle(screen, current_color, (x,y), 3)

        if mode == "eraser":
            pygame.draw.circle(screen, WHITE, (x,y), 10)


    pygame.display.update()
    clock.tick(60)