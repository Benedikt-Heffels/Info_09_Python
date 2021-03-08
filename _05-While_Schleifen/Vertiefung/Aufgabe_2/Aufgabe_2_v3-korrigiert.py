import random

print("Hallo! Willkommen bei Lotto Ben. Bei diesem Spiel müssen Sie 6 Zahlen Tippen.")
print("Die Zahlen müssen zwischen 1 und 49 liegen! Zudem dürfen sich die Zahlen in Ihren Tipps nicht wiederholen.")
Start = input("Wollen Sie fortfahren? ")

if Start == "Ja":
    go = True
else:
    go = False

while go:

    # Man gibt seine Tips ein
    eingabe_beginn = True
    eingabe_liste = []
    anzahl_durchgaenge = 1

    while eingabe_beginn:
        eingabe_zahl = input("Bitte geben Sie nun Ihre Zahl Nummer " + str(
            anzahl_durchgaenge) + " ein. Beachten Sie, dass diese Zahl zwischen 1 und 49 "
                                  "liegen muss und, dass Sie diese Zahl noch nicht getippt haben! ")
        if int(eingabe_zahl) <= 0 or int(eingabe_zahl) >= 50:
            eingabe_zahl_v2 = input(
                "Diese Zahl ist falsch! Bitte versuchen Sie es erneut mit einer Zahl zwischen 1 und 49, die Sie noch nicht getippt haben! ")
            if int(eingabe_zahl_v2) <= 0 or int(eingabe_zahl_v2) >= 50:
                eingabe_zahl_v3 = input(
                    "Die vorherige Zahl war wieder falsch. Bitte versuchen Sie es ein letztes mal erneut"
                    " mit einer Zahl zwischen 1 und 49, die Sie noch nicht getippt haben. Ansonsten wird das Programm beendet!")
                if int(eingabe_zahl_v3) <= 0 or int(eingabe_zahl_v3) >= 50:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                elif eingabe_zahl_v3 in eingabe_liste:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                else:
                    eingabe_liste.append(eingabe_zahl_v3)
            elif eingabe_zahl_v2 in eingabe_liste:  # Überprüft, ob sich Zahlen wiederholen
                eingabe_zahl_v3 = input("Die vorherige Zahl hatten Sie auch bereits getippt. Bitte versuchen Sie es "
                                        "mit einer Zahl, die Sie noch nicht getippt haben und die zwischen 1 und 49 liegt, erneut. Das Programm wird sonst ausgeschaltet. ")
                if int(eingabe_zahl_v3) <= 0 or int(eingabe_zahl_v3) >= 50:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                elif eingabe_zahl_v3 in eingabe_liste:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                else:
                    eingabe_liste.append(eingabe_zahl_v3)
            else:
                eingabe_liste.append(eingabe_zahl_v2)
        elif eingabe_zahl in eingabe_liste:
            eingabe_zahl_v2 = input(
                "Tut mir Leid, diese Zahl ist leider ungültig. Sie können jede Zahl nur einmal Tippen. Beachten Sie bitte auch, "
                "dass Ihre Tipps zwischen 1 und 59 liegen müssenBitte wählen Sie einen neuen Tipp: ")
            if int(eingabe_zahl_v2) <= 0 or int(eingabe_zahl_v2) >= 50:
                eingabe_zahl_v3 = input(
                    "Die vorherige Zahl war wieder falsch. Bitte versuchen Sie es ein letztes mal erneut"
                    " mit einer Zahl zwischen 1 und 49, die Sie noch nicht getippt haben. Ansonsten wird das Programm beendet!")
                if int(eingabe_zahl_v3) <= 0 or int(eingabe_zahl_v3) >= 50:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                elif eingabe_zahl_v3 in eingabe_liste:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                else:
                    eingabe_liste.append(eingabe_zahl_v3)
            elif eingabe_zahl_v2 in eingabe_liste:
                eingabe_zahl_v3 = input("Die vorherige Zahl hatten Sie auch bereits getippt. Bitte versuchen Sie es "
                                        "mit einer Zahl, die Sie noch nicht getippt haben und die zwischen 1 und 49 liegt, erneut. Das Programm wird sonst ausgeschaltet. ")
                if int(eingabe_zahl_v3) <= 0 or int(eingabe_zahl_v3) >= 50:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                elif eingabe_zahl_v3 in eingabe_liste:
                    print("Das Programm 'Lotto Ben' wird nun beendet. Dies tut uns sehr Leid.")
                    print("Hoffentlich können wir Sie demnächst noch einmal Begrüßen!")
                    exit()  # 'exit' beendet das Programm an dieser Stelle
                else:
                    eingabe_liste.append(eingabe_zahl_v3)
            else:
                eingabe_liste.append(eingabe_zahl_v2)
        else:
            eingabe_liste.append(eingabe_zahl)

        anzahl_durchgaenge = anzahl_durchgaenge + 1
        if anzahl_durchgaenge == 7:
            eingabe_beginn = False
        else:
            eingabe_beginn = True

    # Die Gewinnzahlen werden ausgelost
    gewinnzahl_liste = []

    gewinnzahl_ziehen = True
    anzahl_durchgaenge_ziehen = 1

    while gewinnzahl_ziehen:
        gewinnzahl_gezogen = random.randint(1, 49)
        if gewinnzahl_gezogen not in gewinnzahl_liste:
            gewinnzahl_liste.append(gewinnzahl_gezogen)
        if len(gewinnzahl_liste) == 6:
            gewinnzahl_ziehen = False

    # Auflösung: Wie viele Tipps waren richtig?
    anzahl_richtige = gewinnzahl_liste.count(eingabe_liste)

    if anzahl_richtige == 6:
        print("\nGlückwunsch! Alle Ihre Tipps waren richtig. Sie haben den Hauptgewinn gewonnen.")
        weitertippen = input("Wollen Sie Ihren Gewinn erhöhen? ")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    elif anzahl_richtige >= 4:
        print("\nIch gratuliere! Sie hatten ", str(anzahl_richtige), "Tipps!")
        print("Die gezogenen Zahlen lauteten: ", str(gewinnzahl_liste))
        weitertippen = input("Das war eine sehr gute Leistung! Wollen Sie Ihre Leistung erhöhen?")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    elif anzahl_richtige >= 1:
        print("\nSchade. Sie habe leider nur ", str(anzahl_richtige),
              "Tipps gesetzt. Das ist aber trotzdem eine gute Leistung!")
        print("Die gezogenen Zahlen lauteten: ", str(gewinnzahl_liste))
        weitertippen = input("Ihre Leistung war, für den Anfang, gar nicht so schlecht. Wollen Sie sich verbessern?")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    elif anzahl_richtige == 0:
        print("\nDas ist Schade! Sie haben leider kein richtiges Kreuz gesetzt.")
        print("Folgende Zahlen wären richtig gewesen: ", str(gewinnzahl_liste))
        weitertippen = input(
            "Trotzdem: Kopf hoch! Sie kriegen das auch besser hin. Wollen Sie es noch einmal versuchen? ")
        if weitertippen == "Ja":
            go = True
        else:
            go = False
    else:
        print("Wir haben leider gerade ein paar technische Probleme. Bitte starten Sie das Programm neu!")
        exit()

    exit()
