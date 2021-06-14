import pygame
# ---------------Türkis--------Gelb-----------Lila-----------Grün---------Rot----------Blau---------Orange
block_colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]



pygame.init()
pygame.display.set_mode((320, 400))
pygame.display.set_caption("Tetris")

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    # Hier kommen demnächst unsere Funktionen hin!

    pygame.display.update()
