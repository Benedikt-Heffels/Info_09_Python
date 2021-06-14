import pygame

def circle_move_right(start_x, start_y, radius, move_x, move_x_back):
    pygame.draw.circle(win, (255, 0, 0), (start_x + move_x - move_x_back, start_y), radius)


# Hauptteil
pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bewegungen")
bRun = True
step = 0
step_back = 0
while bRun:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bRun = False
    win = pygame.display.get_surface()
    win.fill((0, 0, 0))
    start_x = 50
    circle_move_right(start_x, 250, 50, step*5, step_back*5)

    if start_x + step*5 <= 500:
        # print("Ich bin klein!!!")
        step += 1
    elif start_x + step*5 >= 500:
        step_back += 1
        # print("Ich bin groß!!")

    if start_x + step_back*5 >= 500:
        step_back = 0
        step = 0

    pygame.display.update()
pygame.quit()
