import pygame

board_width = 320
board_height = 400

pygame.init()
pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Tetris")

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    # Hier kommen demnächst unsere Funktionen hin!

    pygame.display.update()
