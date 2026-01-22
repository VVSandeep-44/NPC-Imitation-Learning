import pygame
import sys
import torch
import torch.nn as nn

pygame.init()

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 40
ROWS, COLS = 10, 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NPC Playing using Imitation Learning")

npc_pos = [0, 0]
goal_pos = [8, 8]

clock = pygame.time.Clock()

# Load trained model
model = nn.Sequential(
    nn.Linear(4, 32),
    nn.ReLU(),
    nn.Linear(32, 4)
)
model.load_state_dict(torch.load("model/imitation_model.pth"))
model.eval()

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

def move_npc(action):
    if action == 0:
        npc_pos[1] = max(0, npc_pos[1] - 1)
    elif action == 1:
        npc_pos[1] = min(ROWS - 1, npc_pos[1] + 1)
    elif action == 2:
        npc_pos[0] = max(0, npc_pos[0] - 1)
    elif action == 3:
        npc_pos[0] = min(COLS - 1, npc_pos[0] + 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Prepare state
    state = torch.tensor(
        [npc_pos[0], npc_pos[1], goal_pos[0], goal_pos[1]],
        dtype=torch.float32
    )

    # Predict action
    with torch.no_grad():
        action = torch.argmax(model(state)).item()

    move_npc(action)

    screen.fill((255, 255, 255))
    draw_grid()
    draw_rect(npc_pos, (255, 0, 0))    # NPC
    draw_rect(goal_pos, (0, 255, 0))   # Goal

    pygame.display.update()
    clock.tick(5)
