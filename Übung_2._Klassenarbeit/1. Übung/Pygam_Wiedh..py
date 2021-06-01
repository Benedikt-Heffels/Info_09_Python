import pygame
def zeichne_formen():
    win = pygame.display.get_surface()
    pygame.draw.circle(win, (255, 255, 0), (255, 255), 50)
    pygame.draw.polygon(win, (255, 255, 255), ((0, 0), (18, 189), (200, 255)), 1)
    pygame.draw.line(win, (255, 0, 0), (1, 1), (165, 265), 20)
    pygame.draw.rect(win, (0, 0, 255), (200, 200, 20, 20))




pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("My game")

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False
        zeichne_formen()
    # Hier kommt demnächst unsere Funktionen hin!

    pygame.display.update()

pygame.quit()
