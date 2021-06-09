import random
passwort = [5, 1, 1, 6, 8, 0, 11, 13, 8, 7, 0, 1, 4, 6, 6, 3, 2, 9, 5, 0, 7, 6, 6, 6, 1, 8]
Sonderzeichen = ["#", "!", "?", "%", "$"]

element_y = 0
while element_y <= 4:
    position_sonderzeichen = random.randint(0, 20)
    wahl_sonderzeichen = random.randint(0, 4)
    passwort.pop(position_sonderzeichen)
    passwort.insert(position_sonderzeichen, wahl_sonderzeichen)
    print(passwort)
    element_y += 1

