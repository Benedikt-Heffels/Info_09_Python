spielfeld_mit_nummern = ["",
                         "1", "2", "3",
                         "4", "5", "6",
                         "7", "8", "9"]
spielfeld = ["",
             " ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

spielfeld_leer = ["",
                  " ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " "]


def spielfeld_drucken():
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])


def spielfeld_mit_nummern_drucken():
    print("\t" + spielfeld_mit_nummern[1] + "|" + spielfeld_mit_nummern[2] + "|" + spielfeld_mit_nummern[3])
    print("\t" + spielfeld_mit_nummern[4] + "|" + spielfeld_mit_nummern[5] + "|" + spielfeld_mit_nummern[6])
    print("\t" + spielfeld_mit_nummern[7] + "|" + spielfeld_mit_nummern[8] + "|" + spielfeld_mit_nummern[9])


def setzen(name_spieler_a, name_spieler_b):
    # spielfeld = spielfeld_leer # (Liste leeren)
    symbol_spieler_a = "X"
    symbol_spieler_b = "O"
    spielfeld_drucken()
    kein_sieger = True
    while kein_sieger == True:
        setzung_a = int(input(name_spieler_a + ", bitte gebe die Nummer des Feldes ein, auf das du setzen möchtest: "))
        setzung_a_neu = falsches_feld(setzung_a)
        spielfeld[setzung_a_neu] = symbol_spieler_a
        winning_control(symbol_spieler_a, name_spieler_a, name_spieler_b)
        volles_feld(name_spieler_a, name_spieler_b)
        setzung_b = int(input(name_spieler_b + ", bitte gebe die Nummer des Feldes ein, auf das du setzen möchtest: "))
        setzung_b_neu = falsches_feld(setzung_b)
        spielfeld[setzung_b_neu] = symbol_spieler_b
        winning_control(symbol_spieler_b, name_spieler_a, name_spieler_b)
        volles_feld(name_spieler_a, name_spieler_b)
        spielfeld_drucken()


def spiel_starten():
    print("Willkommen bei Tic, Tac, Toe.")
    print("Die Regeln sind eigentlich ganz einfach: Es gewinnt derjenige, der als erstes drei Felder in einer Reihe"
          " belegt. Hierbei ist es egal, ob die Reihe waagerecht, senkrecht oder schräg zustande kommt!")
    print("Sie werden nachher ihr Symbol setzen, indem Sie die Nummer des Spielfeldes eingeben, auf das sie setzen wollen.")
    print("Das Spielfeld mit Nummern sieht wie folgt aus:")
    spielfeld_mit_nummern_drucken()


def spieler_erstellen_a():
    name_spieler_a = input("Spieler A, du wirst gleich X sein. Bitte gebe doch deinen Namen an: ")
    return name_spieler_a


def spieler_erstellen_b():
    name_spieler_b = input("Spieler B, du wirst gleich O sein. Bitte gebe doch deinen Namen an: ")
    return name_spieler_b


def winning_control(symbol, name_spieler_a, name_spieler_b):
    # Horizontal
    if spielfeld[1] == symbol and spielfeld[2] == symbol and spielfeld[3] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    elif spielfeld[4] == symbol and spielfeld[5] == symbol and spielfeld[6] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    elif spielfeld[7] == symbol and spielfeld[8] == symbol and spielfeld[9] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    # Senkrecht
    elif spielfeld[1] == symbol and spielfeld[4] == symbol and spielfeld[7] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    elif spielfeld[2] == symbol and spielfeld[5] == symbol and spielfeld[8] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    elif spielfeld[3] == symbol and spielfeld[6] == symbol and spielfeld[9] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    # Schräg
    elif spielfeld[1] == symbol and spielfeld[5] == symbol and spielfeld[9] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)
    elif spielfeld[7] == symbol and spielfeld[5] == symbol and spielfeld[3] == symbol:
        if symbol == "X":
            print("Glückwunsch! " + name_spieler_a + " gewinnt.")
        else:
            print("Glückwunsch! " + name_spieler_b + " gewinnt.")
        spielfeld_drucken()
        hauptmenue(name_spieler_a, name_spieler_b)


def falsches_feld(setzung):
    if spielfeld[setzung] == "X" or spielfeld[setzung] == "O":
        setzung_neu = int(input("Ungültiges Feld! Bitte versuche es erneut: "))
        falsches_feld(setzung_neu)
    elif setzung >= 10 or setzung <= 0:
        setzung_neu = int(input("Ungültiges Feld! Bitte versuche es erneut: "))
        falsches_feld(setzung_neu)
    else:
        setzung_neu = setzung
    return setzung_neu


def hauptmenue(name_spieler_a, name_spieler_b):
    print("\nWas möchten sie tun?")
    print("(1): Spiel Starten")
    print("(2): Spiel mit neuen Namen starten")
    print("(3): Spielfeld mit Setzungsnummern anzeigen")
    print("(4) Tic, Tac, Toe verlassen")
    falsche_antwort = True
    while falsche_antwort == True:
        auswahl = int(input("Bitte geben sie ihre Auswahl ein: "))
        if auswahl == 1:
            print("")
            setzen(name_spieler_a, name_spieler_b)
        elif auswahl == 2:
            print("")
            name_spieler_a = spieler_erstellen_a()
            name_spieler_b = spieler_erstellen_b()
            setzen(name_spieler_a, name_spieler_b)
        elif auswahl == 3:
            print("")
            spielfeld_mit_nummern_drucken()
            hauptmenue(name_spieler_a, name_spieler_b)
        elif auswahl == 4:
            print("")
            print("Das ist Schade! Wir hoffen, sie hatten ihren Spielspaß. Bis zum nächsten Mal.")
            falsche_antwort = False
            exit()


def volles_feld(name_spieler_a, name_spieler_b):
    if spielfeld[1] == "X" or spielfeld[1] == "O":
        if spielfeld[2] == "X" or spielfeld[2] == "O":
            if spielfeld[3] == "X" or spielfeld[3] == "O":
                if spielfeld[4] == "X" or spielfeld[4] == "O":
                    if spielfeld[5] == "X" or spielfeld[5] == "O":
                        if spielfeld[6] == "X" or spielfeld[6] == "O":
                            if spielfeld[7] == "X" or spielfeld[7] == "O":
                                if spielfeld[8] == "X" or spielfeld[8] == "O":
                                    if spielfeld[9] == "X" or spielfeld[9] == "O":
                                        print("Leider ist das Spielfeld voll! Das Spiel geht damit leider unentschieden"
                                              " aus.")
                                        hauptmenue(name_spieler_a, name_spieler_b)



spiel_starten()
name_spieler_a = spieler_erstellen_a()
name_spieler_b = spieler_erstellen_b()
hauptmenue(name_spieler_a, name_spieler_b)
