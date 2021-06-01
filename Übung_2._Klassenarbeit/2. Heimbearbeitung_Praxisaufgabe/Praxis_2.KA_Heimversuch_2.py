import random
passwort = []
sonderzeichen = ["!", "$", "?", "%", "#"]


def benutzereingabe():
    print("Ein sicheres Passwort hat zwischen 8 und 20 Zeichen")
    echte_wahl = False
    while echte_wahl == False:
        laenge_pw = int(input("Bitte geben sie ein, wie lange ihr Passwort sein soll: "))
        if laenge_pw >= 8 and laenge_pw <= 20:
            echte_wahl = True
        else:
            print("Falsche Eingabe!")
    return laenge_pw


def passwort_erstellen():
    global laenge_pw
    laenge_liste = 0
    while laenge_liste < laenge_pw:
        zahlen = random.randint(0, 10)
        passwort.append(zahlen)
        laenge_liste += 1
    anzahl_sonderzeichen = 0
    laenge_pw_1 = laenge_pw - 1
    while anzahl_sonderzeichen <= 5:
        pos_sonderzeichen = random.randint(0, laenge_pw_1)
        art_sonderzeichen = random.randint(0, 4)
        random_sonderzeichen = sonderzeichen[art_sonderzeichen]
        passwort.pop(pos_sonderzeichen)
        passwort.insert(pos_sonderzeichen, random_sonderzeichen)
        anzahl_sonderzeichen += 1



laenge_pw = benutzereingabe()
passwort_erstellen()
print("\n\nIhr sicheres und zufälliges Passwort:")
print(passwort)

