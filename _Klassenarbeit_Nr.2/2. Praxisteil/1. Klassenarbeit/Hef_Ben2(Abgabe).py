import random
passwort = []
Sonderzeichen = ["#", "!", "?", "%", "$"]

def eingabe_passwortlänge():
    print("Willkommen beim Passwortgenerator!")
    falsches_passwort = True
    while falsches_passwort:
        print("Wie lange soll ihr Passwort sein? Es muß mindestens 8 und maximal 20 Zeichen enthalten!")
        anzahl_zahlen_passwort = int(input("Ihre Eingabe bitte: "))
        if anzahl_zahlen_passwort >= 7 and anzahl_zahlen_passwort <= 20:
            falsches_passwort = False
        else:
            print("Falsche Eingabe!")

        # anzahl_zahlen_passwort_int = anzahl_zahlen_passwort
    return anzahl_zahlen_passwort

def passwort_erzeugen(gewünschte_länge_passwort):
    element_x = 0
    while element_x <= gewünschte_länge_passwort:
        zufallszahl = random.randint(0, 9)

        passwort.append(zufallszahl)

        element_x += 1
    element_y = 0
    while element_y <= 4:
        position_sonderzeichen = random.randint(0, 20)
        wahl_sonderzeichen = random.randint(0, 4)
        passwort.pop(position_sonderzeichen)
        passwort.insert(position_sonderzeichen, wahl_sonderzeichen)
        element_y += 1




gewünschte_länge_passwort = eingabe_passwortlänge()
passwort_erzeugen(gewünschte_länge_passwort)

print("Ihr sicheres Passwort: " + str(passwort))

