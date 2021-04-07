# Programm, um Schere, Stein, Papier gegen den Computer zu spielen

# Teil 1: Importfunktionen
import random


# ----------------------------------------------------------------------------------------------------------------------
# Teil 2: Listen


liste_wahlmoeglichkeiten = ["Schere", "Stein", "Papier"]


# ----------------------------------------------------------------------------------------------------------------------
# Teil 3: Funktionen


def Computer_zieht():
    Computer_Ziehung = random.randint(0, 2)
    return Computer_Ziehung
    #return liste_wahlmoeglichkeiten[Computer_Ziehung]


def uebersetzung_wahl_mensch(wahl_mensch):
    if wahl_mensch == "Schere":
        zahl_wahl_mensch = 0
    elif wahl_mensch == "Stein":
        zahl_wahl_mensch = 1
    elif wahl_mensch == "Papier":
        zahl_wahl_mensch = 2
    return zahl_wahl_mensch


def wahlanalyse(wahl_computer, zahl_wahl_mensch):
    # Mögliche Fälle:
    # Mensch: Schere (0), Computer: Papier (2) => Sieg Mensch
    # Mensch: Schere (0), Computer: Stein (1) => Sieg Computer
    # Mensch: Stein (1), Computer: Schere (0) => Sieg Mensch
    # Mensch: Stein (1), Computer: Papier (2) => Sieg Computer
    # Mensch: Papier (2), Computer: Schere (0) => Sieg Computer
    # Mensch: Papier (2), Computer: Stein (1) => Sieg Mensch
    # Mensch = Computer => Unentschieden
    print(type(wahl_computer))
    print(type(zahl_wahl_mensch))
    if zahl_wahl_mensch == 0 and wahl_computer == 2:
        print("Du gewinnst!")
        #Sieg Mensch
    elif zahl_wahl_mensch == 0 and wahl_computer == 1:
        print("Der Computer gewinnt!")
        #Sieg PC
    elif zahl_wahl_mensch == 1 and wahl_computer == 0:
        print("Du gewinnst!")
        #Sieg Mensch
    elif zahl_wahl_mensch == 1 and wahl_computer == 2:
        print("Der Computer gewinnt!")
        #Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 0:
        print("Der Computer gewinnt!")
        #Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 1:
        print("Du gewinnst!")
        #Sieg Mensch
    elif zahl_wahl_mensch == wahl_computer:
        print("Unentschieden!")
        #Unentschieden

# ----------------------------------------------------------------------------------------------------------------------
# Teil 4: main


print("Willkommen bei 'schere, Stein, Papier'")
print("Das Spiel wird im Anschluss drei mal gespielt. Wer danach die meisten Punkte hat, gewinnt!")
runden = 0

for runden in range(0, 3):
    wahl_mensch = input("Bitte wählen sie zwischen Schere, Stein und Papier:")
    zahl_wahl_mensch = uebersetzung_wahl_mensch(wahl_mensch) # Type: Integer
    print(type(zahl_wahl_mensch))
    wahl_computer = Computer_zieht()
    #print(wahl_computer)
    #wahlanalyse = wahlanalyse(wahl_computer, zahl_wahl_mensch)
    wahlanalyse(wahl_computer, zahl_wahl_mensch)
    #exit()
    #print(zahl_wahl_mensch)
    #print("Ausführen!")
