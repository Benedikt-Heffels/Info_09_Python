import random

print("Hallo! Willkommen bei Lotto Ben. Bei diesem Spiel müssen sie 6 Zahlen Tippen.")
print("Die Zahlen müssen zwischen 1 und 49 liegen!")
Start = input("Wollen sie fortfahren? ")

if Start == "Ja":
    go = True
else:
    go = False

while go:

    #Man gibt seine Tips ein
    eingabe_beginn = True
    eingabe_liste = []
    anzahl_durchgänge = 1
    while eingabe_beginn:
        eingabe_zahl = input("Bitte geben Sie nun ihre Zahl Nummer " + str(anzahl_durchgänge) + " ein. Beachten Sie, dass diese Zahl zwischen 1 und 49 liegen muss! ")
        if int(eingabe_zahl) <=0 or int(eingabe_zahl) >=50:
            eingabe_zahl_v2 = input("Diese Zahl ist falsch! Bitte versuchen sie es erneut mit einer Zahl zwischen 1 und 49! ")

            if eingabe_zahl_v2 <=0 or eingabe_zahl_v2 >= 50:
                eingabe_zahl_v3 = input("Die vorherige Zahl war wieder falsch. Bitte versuchen sie es ein letztes mal erneut"
                                        " mit einer Zahl zwischen 1 und 49. Ansonsten wird das Programm beendet!")
                if eingabe_zahl_v3 <= 0 or eingabe_zahl_v3 >= 50:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir sie demnächst noch einmal Begrüßen!")
                    exit()  #'exit' beendet das Programm an dieser Stelle
                else:
                    eingabe_liste.append(eingabe_zahl_v3)
            else:
                eingabe_liste.append(eingabe_zahl_v2)
        else:
            eingabe_liste.append(eingabe_zahl)

        anzahl_durchgänge = anzahl_durchgänge + 1
        if anzahl_durchgänge == 7:
            eingabe_beginn = False
        else:
            eingabe_beginn = True

    #Die Gewinnzahlen werden ausgelost
    gewinnzahl_liste = []
    gewinnzahl_gezogen = random.randint(1, 49)
    gewinnzahl_liste.append(gewinnzahl_gezogen)
    print(gewinnzahl_liste)
    #exit()
    gewinnzahl_ziehen = True
    anzahl_durchgänge = 2
    #while gewinnzahl_ziehen:
    gewinnzahl_gezogen = random.randint(1, 49)
    if gewinnzahl_gezogen in gewinnzahl_liste:
        gewinnzahl_gezogen_v2 = random.randint(1, 49)
        if gewinnzahl_gezogen_v2 in gewinnzahl_liste:
            gewinnzahl_gezogen_v3 = random.randint(1, 49)
            if gewinnzahl_gezogen_v3 in gewinnzahl_liste:
                print("\nTut mir Leid! Wir haben derzeit technische Probleme. Bitte versuchen Sie es später erneut.")
                exit()
            else:
                gewinnzahl_liste.append(gewinnzahl_gezogen_v3)
        else:
            gewinnzahl_liste.append(gewinnzahl_gezogen_v2)

    else:
        gewinnzahl_liste.append(gewinnzahl_gezogen)
       # gewinnzahl_liste.append(gewinnzahl_gezogen)
    anzahl_durchgänge = anzahl_durchgänge + 1
    if anzahl_durchgänge == 7:
        gewinnzahlen_ziehen = False
    else:
        gewinnzahlen_ziehen = True
    print(gewinnzahl_liste)
    exit()