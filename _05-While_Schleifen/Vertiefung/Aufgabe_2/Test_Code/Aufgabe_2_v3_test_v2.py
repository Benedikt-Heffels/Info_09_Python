import random
go = True

while go:

    #Man gibt seine Tips ein
    eingabe_beginn = True
    eingabe_liste = []
    anzahl_durchgänge = 1
    while eingabe_beginn:
        eingabe_zahl = input("Bitte geben Sie nun ihre Zahl Nummer " + str(anzahl_durchgänge) + " ein. Beachten Sie, dass diese Zahl zwischen 1 und 49 liegen muss! ")
        if int(eingabe_zahl) <=0 or int(eingabe_zahl) >=50:
            eingabe_zahl_v2 = input("Diese Zahl ist falsch! Bitte versuchen sie es erneut mit einer Zahl zwischen 1 und 49! ")

            if int(eingabe_zahl_v2) <= 0 or int(eingabe_zahl_v2) >= 50:
                eingabe_zahl_v3 = input("Die vorherige Zahl war wieder falsch. Bitte versuchen sie es ein letztes mal erneut"
                                        " mit einer Zahl zwischen 1 und 49. Ansonsten wird das Programm beendet!")
                if int(eingabe_zahl_v3) <= 0 or int(eingabe_zahl_v3) >= 50:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir sie demnächst noch einmal begrüßen!")
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
    #Ziehung 1
    gewinnzahl_gezogen = random.randint(1, 49)
    gewinnzahl_liste.append(gewinnzahl_gezogen)
    #Ziehung 2
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
    #Ziehung 3
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
    #Ziehung 4
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
    #Ziehung 5
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
    #Ziehung 6
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


    anzahl_richtige = gewinnzahl_liste.count(eingabe_liste)
    if anzahl_richtige == 6:
        print("\nGlückwunsch! Alle Ihre Tipps waren richtig. Sie haben den Hauptgewinn gewonnen.")
        weitertippen = input("Wollen Sie ihren Gewinn erhöhen? ")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    elif anzahl_richtige >= 4:
        print("\nIch gratuliere! Sie hatten ", str(anzahl_richtige), "Tipps!")
        print("Die gezogenen Zahlen lauteten: ", str(gewinnzahl_liste))
        weitertippen = input("Das war eine sehr gute Leistung! Wollen Sie ihre Leistung erhöhen?")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    elif anzahl_richtige >= 1:
        print("\nSchade. Sie habe leider nur ", str(anzahl_richtige), "Tipps gesetzt. Das ist aber trotzdem eine gute Leistung!")
        print("Die gezogenen Zahlen lauteten: ", str(gewinnzahl_liste))
        weitertippen = input("Ihre Leistung war, für den Anfang, gar nicht so schlecht. Wollen Sie sich verbessern?")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    elif anzahl_richtige == 0:
        print("\nDas ist Schade! Sie haben leider kein richtiges Kreuz gesetzt.")
        print("Folgende Zahlen wären richtig gewesen: ", str(gewinnzahl_liste))
        weitertippen = input("Trotzdem: Kopf hoch! Sie kriegen das auch besser hin. Wollen Sie es noch einmal versuchen? ")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    else:
        print("Wir haben leider gerade ein paar technische Probleme. Bitte starten Sie das Programm neu!")
        exit()

    exit()