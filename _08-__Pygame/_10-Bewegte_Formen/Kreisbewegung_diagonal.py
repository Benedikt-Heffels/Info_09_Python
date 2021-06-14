import pygame

# Hauptteil
pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bewegungen")

circle_x = 50
circle_y = 50
circle_r = 50

bRun = True
while bRun:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False
    win = pygame.display.get_surface()
    win.fill((0, 0, 0))
    circle_x += 5
    circle_y += 5
    pygame.draw.circle(win, (255, 0, 0), (circle_x, circle_y), circle_r)
    pygame.display.update()
pygame.quit()
