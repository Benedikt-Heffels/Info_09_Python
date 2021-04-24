# ---------------------------------------------------- Listen ----------------------------------------------------------
Spielfeld = [["Zeile 0:", "\t", "1", " | ", "2", " | ", "3"],
             ["Zeile 1:", "\t", " ",  " | ", " ", " | ", " "],
             ["Zeile 2:\t"," ", " | ", " ", " | ", " "],
             ["Zeile 3:\t", " ", " | ", " ", " | ", " "]]

# --------------------------------------------------- Funktionen -------------------------------------------------------


def Spieler():
    print("Willkommen bei Tic-Tac-Toe!")
    print("Dieses Spiel spielt ihr gegeneinander! Die Regeln sind folgende: Es erscheint gleich ein drei-mal drei Feld. "
          "Hier müsst ihr eure Simbole eingeben. Wer zuerst eine dreier-Reihe mit seinem Symbol gefüllt hat, der hat "
          "gewonnen!")
    print("Ihr müsst bitte gleich die Koordinaten eures Feldes angeben.")
    Namen = input("Wollt ihr eure Namen angeben? (Ja/Nein): ")
    if Namen == "Ja":
        Name_SP1 = input("Spieler 1, gebe bitte hier deinen Namen ein: ")
        Namen_SP2 = input("Spieler 2, gebe bitte hier deinen Namen ein: ")
    else:
        print("Ihr werdet nun als Spieler 1 und Spieler 2 angesprochen.")
    return Name_SP1
    return Name_SP2


def Spiel(Name_SP1, Name_SP2):
    spielen = True
    for spiel in Spielfeld:
        print("h")
# ---------------------------------------------------- Hauptteil -------------------------------------------------------
print(Spielfeld)
for ich in Spielfeld:
    print(ich)