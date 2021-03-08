import random

print("Hallo! Willkommen bei Lotto Ben. Bei diesem Spiel müssen sie 6 Zahlen Tippen.")
print("Die Zahlen müssen zwischen 1 und 49 liegen!")
Start = input("Wollen sie fortfahren? ")

if Start == "Ja":
    go = True
else:
    go = False

while go:
    liste_eingabe = []
    #Die Zahlen werden eingegeben
    zahl1 = input("Bitte geben sie ihre erste Zahl ein: ")
    if int(zahl1) >= 49 or int(zahl1) <= 0:
        print("Falsche Zahl")
        zahl1neu = input("Bitte geben sie ihre erste Zahl erneut ein. Achten sie darauf, dass sie zwischen 1 und 49 liegt! ")
        if int(zahl1neu) >= 49 or int(zahl1neu) <= 0:
            print("falsche Zahl")
        else:
            liste_eingabe.append(zahl1neu)
    else:
        liste_eingabe.append(zahl1)
    zahl2 = input("Bitte geben sie ihre zweite Zahl ein: ")
    if int(zahl2) >= 49 or int(zahl2) <= 0:
        print("Falsche Zahl")
        zahl2neu = input(
            "Bitte geben sie ihre erste Zahl erneut ein. Achten sie darauf, dass sie zwischen 1 und 49 liegt! ")
        if int(zahl2neu) >= 49 or int(zahl2neu) <= 0:
            print("falsche Zahl")
        else:
            liste_eingabe.append(zahl2neu)
    else:
        liste_eingabe.append(zahl1)
    zahl3 = input("Bitte geben sie ihre dritte Zahl ein: ")
    liste_eingabe.append(zahl3)
    zahl4 = input("Bitte geben sie ihre vierte Zahl ein: ")
    liste_eingabe.append(zahl4)
    zahl5 = input("Bitte geben sie ihre fünfte Zahl ein: ")
    liste_eingabe.append(zahl5)
    zahl6 = input("Bitte geben sie ihre sechste Zahl ein: ")
    liste_eingabe.append(zahl6)
    #print(liste_eingabe)

    retry = True
    while retry:
        lösung1 = random.randint(0, 49)
        lösung2 = random.randint(0, 49)
        lösung3 = random.randint(0, 49)
        lösung4 = random.randint(0, 49)
        lösung5 = random.randint(0, 49)
        lösung6 = random.randint(0, 49)


        if lösung1 == lösung2 or lösung1 == lösung3 or lösung1 == lösung4 or lösung1 == lösung5 or lösung1 == lösung6:
            retry = True
        else:
            if lösung2 == lösung3 or lösung2 == lösung4 or lösung2 == lösung5 or lösung2 == lösung6:
                retry = True
            else:
                if lösung3 == lösung4 or lösung3 == lösung5 or lösung3 == lösung6:
                    retry = True
                else:
                    if lösung4 == lösung5 or lösung4 == lösung6:
                        retry = True
                    else:
                        if lösung5 == lösung6:
                            retry = True
                        else:
                            lösungen = [lösung1, lösung2, lösung3, lösung4, lösung5, lösung6]
                            retry = False
    print(lösungen)

    go = False