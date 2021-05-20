import pygame
def zeichnen_formen():
    pygame.draw.rect((0, 0, 255), (0, 0, 20, 20))





















import random
# Das Lottoprogramm soll schauen, ob die Benutzereingabe mit der random-Zahl des PCs übereinstimmt!


eingabe = int(input("Eine Zahl bitte: "))

ziehung = random.randint(1, 40)

if ziehung <= 0 and ziehung >= 40:
    print("Glückwunsch! Sie haben gewonnen!")


