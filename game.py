import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 40
ROWS, COLS = 10, 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Game - Player Movement")

player_pos = [0, 0]
goal_pos = [8, 8]

clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))

def draw_rect(pos, color):
    pygame.draw.rect(
        screen,
        color,
        (pos[0]*GRID_SIZE, pos[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_pos[1] = max(0, player_pos[1] - 1)
            elif event.key == pygame.K_DOWN:
                player_pos[1] = min(ROWS - 1, player_pos[1] + 1)
            elif event.key == pygame.K_LEFT:
                player_pos[0] = max(0, player_pos[0] - 1)
            elif event.key == pygame.K_RIGHT:
                player_pos[0] = min(COLS - 1, player_pos[0] + 1)

    screen.fill((255, 255, 255))
    draw_grid()
    draw_rect(player_pos, (0, 0, 255))   # Player
    draw_rect(goal_pos, (0, 255, 0))     # Goal

    pygame.display.update()
    clock.tick(10)
