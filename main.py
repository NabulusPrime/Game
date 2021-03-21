import pygame
from Tetris import *
from Figure import *

# https://youtu.be/SfPWCKTHzE4?t=2410

colors = [
    (0, 0, 0),
    (0, 240, 240),  # 4 in einer Reihe
    (0, 0, 240),  # Reverse L
    (240, 160, 0),  # L
    (240, 240, 0),  # Block
    (0, 240, 0),    # S
    (160, 0, 240),  # T
    (240, 0, 0)  # Reverse S
]

pygame.init()

screen = pygame.display.set_mode((360, 750))
pygame.display.set_caption("Tetris")

done = False
fps = 25
clock = pygame.time.Clock()
counter = 0
zoom = 30

game = Tetris(10, 24)
pressing_down, pressing_left, pressing_right = False, False, False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                pressing_left = True
            if event.key == pygame.K_RIGHT:
                pressing_right = True

        if pressing_down:
            game.down()
        if pressing_left:
            game.left()
        if pressing_right:
            game.right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False
            if event.key == pygame.K_LEFT:
                pressing_left = False
            if event.key == pygame.K_RIGHT:
                pressing_right = False

    screen.fill(color=WHITE)
    for i in range(game.height):
        for j in range(game.width):
            if game.field[i][j] == 0:
                color = GRAY
                just_border = 1
            else:
                color = colors[game.field[i][j]]
                just_border = 0
            pygame.draw.rect(screen, color, [20+j*zoom, 10+i*zoom, zoom, zoom], just_border)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
