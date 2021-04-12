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


def uebersetzung_wahl_mensch(wahl_mensch):
    if wahl_mensch == "Schere":
        zahl_wahl_mensch = 0
    elif wahl_mensch == "Stein":
        zahl_wahl_mensch = 1
    elif wahl_mensch == "Papier":
        zahl_wahl_mensch = 2
    return zahl_wahl_mensch


    # Mögliche Fälle:
    # Mensch: Schere (0), Computer: Papier (2) => Sieg Mensch
    # Mensch: Schere (0), Computer: Stein (1) => Sieg Computer
    # Mensch: Stein (1), Computer: Schere (0) => Sieg Mensch
    # Mensch: Stein (1), Computer: Papier (2) => Sieg Computer
    # Mensch: Papier (2), Computer: Schere (0) => Sieg Computer
    # Mensch: Papier (2), Computer: Stein (1) => Sieg Mensch
    # Mensch = Computer => Unentschieden


def wahlanalyse(wahl_computer, zahl_wahl_mensch):
    if zahl_wahl_mensch == 0 and wahl_computer == 2:
        print("Du gewinnst!")
        # Sieg Mensch
    elif zahl_wahl_mensch == 0 and wahl_computer == 1:
        print("Der Computer gewinnt!")
        # Sieg PC
    elif zahl_wahl_mensch == 1 and wahl_computer == 0:
        print("Du gewinnst!")
        # Sieg Mensch
    elif zahl_wahl_mensch == 1 and wahl_computer == 2:
        print("Der Computer gewinnt!")
        # Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 0:
        print("Der Computer gewinnt!")
        # Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 1:
        print("Du gewinnst!")
        # Sieg Mensch
    elif zahl_wahl_mensch == wahl_computer:
        print("Unentschieden!")
        # Unentschieden


def wahlanalyse_punkte_mensch(wahl_computer, zahl_wahl_mensch, punkte_mensch, punkte_computer):
    if zahl_wahl_mensch == 0 and wahl_computer == 2:
        punkte_mensch =+ 1
        # Sieg Mensch
    elif zahl_wahl_mensch == 0 and wahl_computer == 1:
        punkte_computer =+ 1
        # Sieg PC
    elif zahl_wahl_mensch == 1 and wahl_computer == 0:
        punkte_mensch = + 1
        # Sieg Mensch
    elif zahl_wahl_mensch == 1 and wahl_computer == 2:
        punkte_computer = + 1
        # Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 0:
        punkte_computer =+ 1
        # Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 1:
        punkte_mensch = + 1
        # Sieg Mensch
    return punkte_mensch


def wahlanalyse_punkte_computer(wahl_computer, zahl_wahl_mensch, punkte_mensch, punkte_computer):
    if zahl_wahl_mensch == 0 and wahl_computer == 2:
        punkte_mensch =+ 1
        # Sieg Mensch
    elif zahl_wahl_mensch == 0 and wahl_computer == 1:
        punkte_computer =+ 1
        # Sieg PC
    elif zahl_wahl_mensch == 1 and wahl_computer == 0:
        punkte_mensch = + 1
        # Sieg Mensch
    elif zahl_wahl_mensch == 1 and wahl_computer == 2:
        punkte_computer = + 1
        # Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 0:
        punkte_computer =+ 1
        # Sieg PC
    elif zahl_wahl_mensch == 2 and wahl_computer == 1:
        punkte_mensch = + 1
        # Sieg Mensch
    return punkte_computer


# ----------------------------------------------------------------------------------------------------------------------
# Teil 4: main


print("Willkommen bei 'schere, Stein, Papier'")
print("Das Spiel wird im Anschluss drei mal gespielt. Wer danach die meisten Punkte hat, gewinnt!")

runden = 0
punkte_mensch = 0
punkte_computer = 0

for runden in range(0, 3):
    wahl_mensch = input("Bitte wählen sie zwischen Schere, Stein und Papier: ")
    zahl_wahl_mensch = uebersetzung_wahl_mensch(wahl_mensch)
    wahl_computer = Computer_zieht()
    print("Computer wählt " + liste_wahlmoeglichkeiten[wahl_computer] + ".")
    wahlanalyse(wahl_computer, zahl_wahl_mensch)
    punkte_mensch_analyse = wahlanalyse_punkte_mensch(wahl_computer, zahl_wahl_mensch, punkte_mensch, punkte_computer)
    punkte_mensch = punkte_mensch + punkte_mensch_analyse
    punkte_computer_analyse = wahlanalyse_punkte_computer(wahl_computer, zahl_wahl_mensch, punkte_mensch, punkte_computer)
    punkte_computer =+ punkte_computer_analyse

print("\n\tEndstand:")
print("\t" + str(punkte_computer) + " Punkt(e) für den Computer und " + str(punkte_mensch) + " Punkt(e) für dich!")
if punkte_computer < punkte_mensch:
    print("\tDamit gewinnst du das Spiel! Glückwunsch!")
elif punkte_computer > punkte_mensch:
    print("\tLeider gewinnt der Computer dieses Spiel!")
else:
    print("\tDamit geht das Spiel unentschieden aus!")
