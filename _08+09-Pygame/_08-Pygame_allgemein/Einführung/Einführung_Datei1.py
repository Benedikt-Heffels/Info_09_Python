import pygame

pygame.init()
pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Das ist mein Spiel")

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    # Hier kommen demnächst unsere Funktionen hin!

    pygame.display.update()

pygame.quit()
