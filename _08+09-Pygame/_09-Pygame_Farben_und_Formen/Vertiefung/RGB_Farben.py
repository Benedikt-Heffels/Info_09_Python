import pygame


def farben_zeichnen():
    global win
    feld_punkt_breite = 0
    feld_punkt_hoehe = 0
    farb_felder_zeichnen = True
    while farb_felder_zeichnen:
        for farbe_rot in range(0, 256, 36):
            for farbe_gruen in range(0, 256, 36):
                for farbe_blau in range(0, 256, 36):
                    pygame.draw.rect(win, (farbe_rot, farbe_gruen, farbe_blau), (feld_punkt_breite, feld_punkt_hoehe,
                                                                                 20, 20))
                    pygame.draw.rect(win, (255, 255, 255), (feld_punkt_breite, feld_punkt_hoehe, 20, 20), 1)
                    feld_punkt_breite += 20
                    if feld_punkt_breite >= 480:
                        feld_punkt_hoehe += 20
                        feld_punkt_breite = 0
        farb_felder_zeichnen = False


# ------------------------------------ Hauptteil -----------------------------------------------------------------------
pygame.init()
pygame.display.set_mode((480, 440))
pygame.display.set_caption("Farben mit RGB-Werten")

win = pygame.display.get_surface()
bRun = True
while bRun:
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 480, 440))
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False
    farben_zeichnen()

    pygame.display.update()

pygame.quit()
