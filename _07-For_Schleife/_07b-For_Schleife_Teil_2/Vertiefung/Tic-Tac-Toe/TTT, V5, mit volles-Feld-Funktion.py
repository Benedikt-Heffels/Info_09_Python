z1 = ["1.1", "1.2", "1.3"]
z2 = ["2.1", "2.2", "2.3"]
z3 = ["3.1", "3.2", "3.3"]
spielfeld = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
spielfeld_leer = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def hauptmenue():
    print("\nWillkommen im Hauptmenü von Tic, Tac, Toe!")
    print("Was willst du tun?")
    print("(1) Spiel spielen")
    print("(2) Programm beenden")
    auswahl = input("Bitte gebe hier die Zahl deiner Wahl ein: ")
    falsche_antwort = True
    while falsche_antwort:
        if auswahl == "1":
            spielen()
        elif auswahl == "2":
            falsche_antwort = False


def spielen():
    spielfeld.clear()
    spielfeld.extend(spielfeld_leer)
    print("\nBitte gebe den gewünschten Punkt gleich in Form von Koordinaten ein (z.B. 1.1 für das erste Kästchen oben "
          "rechts). Beachte: Erst laufen, dann fallen!\n")
    spieler_x = "X"
    spieler_o = "0"
    spiel_spielen = True
    while spiel_spielen:
        for element in spielfeld:
            print(element[0] + " | " + element[1] + " | " + element[2])
            print("----------")
        setzen_x = input("Spieler X, wo möchtest du setzen? ")
        setzen_x_kontrolliert = falsches_feld(setzen_x)
        in_liste_einsetzen(setzen_x_kontrolliert, spieler_x)
        sieg(spieler_x)
        volles_spielfeld()
        setzen_o = input("Spieler 0, wo möchtest du setzen? ")
        setzen_o_kontrolliert = falsches_feld(setzen_o)
        in_liste_einsetzen(setzen_o_kontrolliert, spieler_o)
        sieg(spieler_o)
        volles_spielfeld()


def falsches_feld(setzung):
    if setzung in z1:
        if setzung == "1.1":
            if spielfeld[0][0] == "X" or spielfeld[0][0] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
        elif setzung == "1.2":
            if spielfeld[0][1] == "X" or spielfeld[0][1] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
        elif setzung == "1.3":
            if spielfeld[0][2] == "X" or spielfeld[0][2] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
    elif setzung in z2:
        if setzung == "2.1":
            if spielfeld[1][0] == "X" or spielfeld[1][0] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
        elif setzung == "2.2":
            if spielfeld[1][1] == "X" or spielfeld[1][1] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
        elif setzung == "2.3":
            if spielfeld[1][2] == "X" or spielfeld[1][2] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
    elif setzung in z3:
        if setzung == "3.1":
            if spielfeld[2][0] == "X" or spielfeld[2][0] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
        elif setzung == "3.2":
            if spielfeld[2][1] == "X" or spielfeld[2][1] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
        elif setzung == "3.3":
            if spielfeld[2][2] == "X" or spielfeld[2][2] == "0":
                print("Dieses Spielfeld ist leider schon besetzt. Hier ist das gesamte Spielfeld noch einmal: ")
                for element in spielfeld:
                    print(element[0] + " | " + element[1] + " | " + element[2])
                    print("----------")
                setzung_neu = input("Bitte wähle nun ein unbesetztes Spielfeld: ")
                falsches_feld(setzung_neu)
                return setzung_neu
            else:
                return setzung
    else:
        print("Dieses Spielfeld existiert leider nicht. Das gesamte Spielfeld ist 3 mal 3 gorß, also wähle bitte aus "
              "Zahlen zwischen 1 und 3! Hier siehst du nocheinmal das gesamte Spielfeld: ")
        for element in spielfeld:
            print(element[0] + " | " + element[1] + " | " + element[2])
            print("----------")
        setzung_neu = input("Bitte wähle nun ein existierendes Spielfeld: ")
        falsches_feld(setzung_neu)
        return setzung_neu


def in_liste_einsetzen(setzung, spieler):
    if setzung in z1:
        if setzung == "1.1":
            spielfeld[0][0] = spieler
        elif setzung == "1.2":
            spielfeld[0][1] = spieler
        elif setzung == "1.3":
            spielfeld[0][2] = spieler
    elif setzung in z2:
        if setzung == "2.1":
            spielfeld[1][0] = spieler
        elif setzung == "2.2":
            spielfeld[1][1] = spieler
        elif setzung == "2.3":
            spielfeld[1][2] = spieler
    elif setzung in z3:
        if setzung == "3.1":
            spielfeld[2][0] = spieler
        elif setzung == "3.2":
            spielfeld[2][1] = spieler
        elif setzung == "3.3":
            spielfeld[2][2] = spieler


def sieg(spieler):
    # Horizontal
    if spielfeld[0][0] == spieler and spielfeld[0][1] == spieler and spielfeld[0][2] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    elif spielfeld[1][0] == spieler and spielfeld[1][1] == spieler and spielfeld[1][2] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    elif spielfeld[2][0] == spieler and spielfeld[2][1] == spieler and spielfeld[2][2] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    # Vertikal
    elif spielfeld[0][0] == spieler and spielfeld[1][0] == spieler and spielfeld[2][0] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    elif spielfeld[0][1] == spieler and spielfeld[1][1] == spieler and spielfeld[2][1] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    elif spielfeld[0][2] == spieler and spielfeld[1][2] == spieler and spielfeld[2][2] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    # Schräg
    elif spielfeld[0][0] == spieler and spielfeld[1][1] == spieler and spielfeld[2][2] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()
    elif spielfeld[0][2] == spieler and spielfeld[1][1] == spieler and spielfeld[2][0] == spieler:
        print("Spieler " + spieler + " gewinnt.")
        hauptmenue()


def volles_spielfeld():
        if spielfeld[0][0] == "X" or spielfeld[0][0] == "0":
            if spielfeld[0][1] == "X" or spielfeld[0][1] == "0":
                if spielfeld[0][2] == "X" or spielfeld[0][2] == "0":
                    if spielfeld[1][0] == "X" or spielfeld[1][0] == "0":
                        if spielfeld[1][1] == "X" or spielfeld[1][1] == "0":
                            if spielfeld[1][2] == "X" or spielfeld[1][2] == "0":
                                if spielfeld[2][0] == "X" or spielfeld[2][0] == "0":
                                    if spielfeld[2][1] == "X" or spielfeld[2][1] == "0":
                                        if spielfeld[2][2] == "X" or spielfeld[2][2] == "0":
                                            print("Das Spielfeld ist voll! Damit ging das Spiel leider unentschieden "
                                                  "aus.")
                                            spielfeld.clear()
                                            spielfeld.extend(spielfeld_leer)
                                            hauptmenue()


hauptmenue()
