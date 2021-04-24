Z1 = ["1.1", "1.2", "1.3"]
Z2 = ["2.1", "2.2", "2.3"]
Z3 = ["3.1", "3.2", "3.3"]

# Spielfeld = [["Zeile 0:\t", "1", "|", "2", "|", "3"],
#              ["Zeile 1:\t", " ", "|", " ", "|", " "],
#              ["Zeile 2:\t", " ", "|", " ", "|", " "],
#              ["Zeile 3:\t", " ", "|", " ", "|", " "]]
Spielfeld = [[" ", "1", "2", "3"], ["1", " ", " ", " "], ["2", " ", " ", " "], ["3", " ", " ", " "]]

def Spiel():
    go = True
    Spieler_A = "X"
    Spieler_B = "0"
    while go == True:
        for spiel in Spielfeld:
            print(spiel)
        Setzen_A = input("Spieler 1: Wo möchtest du setzen? Bitte gebe die Koordinaten an: ")
        In_Liste_Einsetzen_A = Koordinaten_Spielfeld(Setzen_A, Spieler_A)
        Sieg_A = Sieg(Spieler_A)
        Setzen_B = input("Spieler 2: Wo möchtest du setzen? Bitte gebe die Koordinaten an: ")
        In_Liste_Einsetzen_B = Koordinaten_Spielfeld(Setzen_B, Spieler_B)
        Sieg_B = Sieg(Spieler_B)




def Koordinaten_Spielfeld(Setzung, Spieler):
    if Setzung in Z1:
        if Setzung == "1.1":
            Spielfeld[1][1] = Spieler
        elif Setzung == "1.2":
            Spielfeld[1][2] = Spieler
        elif Setzung == "1.3":
            Spielfeld[1][3] = Spieler
    elif Setzung in Z2:
        if Setzung == "2.1":
            Spielfeld[2][1] = Spieler
        elif Setzung == "2.2":
            Spielfeld[2][2] = Spieler
        elif Setzung == "2.3":
            Spielfeld[2][3] = Spieler
    elif Setzung in Z3:
        if Setzung == "3.1":
            Spielfeld[3][1] = Spieler
        elif Setzung == "3.2":
            Spielfeld[3][2] = Spieler
        elif Setzung == "3.3":
            Spielfeld[3][3] = Spieler

def Sieg(Spieler):
    go = True
    # Horizontal
    if Spielfeld[1] == Spieler or Spielfeld[2] == Spieler or Spielfeld[3] == Spieler:
        print("Sieg für " + Spieler)
        go = False
    # Vertikal
    elif Spielfeld[1][1] == Spieler and Spielfeld[2][1] == Spieler and Spielfeld[3][1] == Spieler:
        print("Sieg für " + Spieler)
        go = False
    elif Spielfeld[1][2] == Spieler and Spielfeld[2][2] == Spieler and Spielfeld[3][2] == Spieler:
        print("Sieg für " + Spieler)
        go = False
    elif Spielfeld[1][3] == Spieler and Spielfeld[2][3] == Spieler and Spielfeld[3][3] == Spieler:
        print("Sieg für " + Spieler)
        go = False
    # Schräg
    elif Spielfeld[1][1] == Spieler and Spielfeld[2][2] == Spieler and Spielfeld[3][3] == Spieler:
        print("Sieg für " + Spieler)
        go = False
    elif Spielfeld[3][1] == Spieler and Spielfeld[2][2] == Spieler and Spielfeld[1][3] == Spieler:
        print("Sieg für " + Spieler)
        go = False
    return go


def falsches_feld(Setzung, Spieler):
    if Setzung in Z1:
        if Setzung == "1.1":
            if Spielfeld[1][1] == "X" or Spielfeld [1][1] == "O":
                Setzung_Neu = int(input("Dieses Feld ist bereits belegt oder nicht wählbar! Bitte versuche es erneut: "))
        elif Setzung == "1.2":
            Spielfeld[1][2] = Spieler
        elif Setzung == "1.3":
            Spielfeld[1][3] = Spieler
    elif Setzung in Z2:
        if Setzung == "2.1":
            Spielfeld[2][1] = Spieler
        elif Setzung == "2.2":
            Spielfeld[2][2] = Spieler
        elif Setzung == "2.3":
            Spielfeld[2][3] = Spieler
    elif Setzung in Z3:
        if Setzung == "3.1":
            Spielfeld[3][1] = Spieler
        elif Setzung == "3.2":
            Spielfeld[3][2] = Spieler
        elif Setzung == "3.3":
            Spielfeld[3][3] = Spieler


print("Spieler 1 ist X und Spieler 2 ist O")
Start = Spiel()