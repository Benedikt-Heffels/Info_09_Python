import pygame

def zeichne_formen():
    win = pygame.display.get_surface()
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 30, 30))
    pygame.draw.rect(win, (255, 255, 0), (0, 40, 50, 1))
    # pygame.draw.rect(win, (0, 255, 0), (470, 470, 30, 30))
    # pygame.draw.rect(win, (0, 0, 255), (0, 470, 30, 30))
    # pygame.draw.rect(win, (255, 255, 0), (470, 0, 30, 30))
    #
    # pygame.draw.circle(win, (0, 255, 0), (50, 50), 20)
    # pygame.draw.line(win, (0, 255, 255), (100, 0), (100, 500), 5)
    # pygame.draw.line(win, (0, 150, 150), (0, 100), (500, 100), 5)
    # pygame.draw.rect(win, (255, 255, 255), (150, 150, 200, 125), 5)
    # pygame.draw.ellipse(win, (255, 0, 255), (150, 150, 200, 125), 5)
    pygame.draw.polygon(win, (125, 125, 125), ((300, 350), (250, 400), (350, 400)), 5)


pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("Das ist mein Spiel")

bRun = True
while bRun:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    zeichne_formen()
    # Hier kommen demnächst unsere Funktionen hin!

    pygame.display.update()

pygame.quit()
