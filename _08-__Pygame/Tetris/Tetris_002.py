import pygame
import random

# ---------------Türkis--------Gelb-----------Lila-----------Grün---------Rot----------Blau---------Orange
block_colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]


block_size = 20
board_width = block_size * 16
board_height = block_size * 20
block_speed = 5
block_x = random.randint(0, 380)
block_y = 50
random_color = random.randint(0, 6)


pygame.init()
pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Tetris")
win = pygame.display.get_surface()
bRun = True
while bRun:
    pygame.time.delay(100)
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    pygame.draw.rect(win, block_colors[random_color], (block_x, block_y + block_speed, block_size, block_size))
    block_speed += 5
    if block_speed == block_size * 20 - 70:
        block_speed = 0
        random_color = random.randint(0, 6)
        block_x = random.randint(0, 380)

    pygame.display.update()
