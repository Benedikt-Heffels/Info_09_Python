import pygame

pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("My game")

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    # Hier kommt demnächst unsere Funktionen hin!

    pygame.display.update()

pygame.quit()
