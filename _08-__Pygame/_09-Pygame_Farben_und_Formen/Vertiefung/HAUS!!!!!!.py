import pygame


def zeichnen_des_hauses():
    global win
    pygame.draw.rect(win, (38, 2, 2), (300, 220, 20, 60))  # Schornstein
    pygame.draw.rect(win, (255, 0, 0), (150, 300, 200, 400))  # Haus
    pygame.draw.polygon(win, (61, 57, 57), ((150, 300), (350, 300), (250, 200)))  # Dach
    pygame.draw.rect(win, (133, 122, 122), (245, 450, 20, 50))  # Tür
    pygame.draw.rect(win, (165, 240, 237), (175, 320, 50, 50))  # Fenster 1
    pygame.draw.rect(win, (165, 240, 237), (275, 320, 50, 50))  # Fenster 2
    pygame.draw.rect(win, (165, 240, 237), (175, 390, 50, 50))  # Fenster 3
    pygame.draw.rect(win, (165, 240, 237), (275, 390, 50, 50))  # Fenster 2


pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("HAUS!!!!!!")
win = pygame.display.get_surface()
bRun = True
while bRun:
    pygame.time.delay(100)
    pygame.draw.rect(win, (194, 209, 208), (0, 0, 500, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False

    zeichnen_des_hauses()

    pygame.display.update()

pygame.quit()
