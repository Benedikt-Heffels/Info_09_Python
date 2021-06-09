import random

liste = ["1","2", "3", "4", "5", "6", "7", "8", "9", "10"]

print(liste)
zuloeschendeselement = int(input("Welches Element möchten sie aus ihrer Liste löschen?"))

loeschposition = zuloeschendeselement - 1

liste.pop(loeschposition)

print(liste)