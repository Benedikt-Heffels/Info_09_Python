#INFOS:
#Schere = 1
#Stein = 2
# Papier = 3
import random
# ------- Funktionen -------

def Ziehung():
    Wahlzahl_PC = random.randint(1, 3)
    Auswertung_Ziehung(Wahlzahl_PC)


def Auswertung_Ziehung(Wahlzahl_PC):
    if Wahlzahl_PC == 1:
        print("Computer wählt Schere!")
    elif Wahlzahl_PC == 2:
        print("Computer wählt Stein!")
    elif Wahlzahl_PC == 3:
        print("Computer wählt Papier!")


def Punkte_Human(Wahl_Human):
    if Wahl_Human == "Schere":
        Wahlzahl_Human = 1
    elif Wahl_Human == "Stein":
        Wahlzahl_Human = 2
    elif Wahl_Human == "Papier":
        Wahlzahl_Human = 3
    else:
        print("ICh habe die Eingabe leider nicht verstanden. Das Programm wird beendet!")
        exit()
    return Wahlzahl_Human

def Wahlanalyse(Wahlzahl_Human, Wahlzahl_PC):
    Punkte_Mensch = 0
    if Wahlzahl_Human == 1 and Wahlzahl_PC == 3:
        print("Gewonnen, H")
        Punkte_Mensch =+ 1
    elif Wahlzahl_Human == 2 and Wahlzahl_PC == 1:
        print("Gewonnen, H")
        Punkte_Mensch = + 1
    elif Wahlzahl_Human == 3 and Wahlzahl_PC == 2:
        print("Gewonnen, H")
        Punkte_Mensch = + 1
    elif Wahlzahl_Human == Wahlzahl_PC:
        print("Unentschieden!")
    else:
        print("Gewonnen, PC")
    return Punkte_Mensch

def Wahlanalyse_Punkt_PC(Wahlzahl_Human, Wahlzahl_PC):
    if Wahlzahl_Human == 1 and Wahlzahl_PC == 3:
        Punkte_Mensch =+ 1
    elif Wahlzahl_Human == 2 and Wahlzahl_PC == 1:
        Punkte_Mensch = + 1
    elif Wahlzahl_Human == 3 and Wahlzahl_PC == 2:
        Punkte_Mensch = + 1
    elif Wahlzahl_Human == Wahlzahl_PC:
        Punkte_Unentschieden =+ 1
    else:
        Punkte_PC =+ 1
    return Punkte_PC




# -------Hauptteil ---------
print("Willkommen bei 'Schere, Stein, Papier'!")
Spielregeln = input("Sie kennen doch sicherlich noch die Spielregeln von 'Schere, Stein, Papier', oder? (Ja/Nein) ")

if Spielregeln == "Nein":
    print("\tSchere schlägt Papier, Stein schlägt Schere, Papier schlägt Stein")
    print("\t Es werden drei Runden gespielt. Für jede gewonnene Runde gibt es einen Punkt.Wählen Benutzer und "
          "Computer das gleiche Element, bekommt niemand einen Punkt.")
    print("\tWer am Ende die meisten Punkte hat, gewinnt!")

#Punkte_Mensch = 0
#Punkte_PC = 0
Runden = 0
for Runden in range(3):
    Wahl_Human = input("Bitte gebe deine Wahl ein: Schere/Stein/Papier ")
    Wahlzahl_PC = Ziehung()
    Wahlzahl_Human = Punkte_Human(Wahl_Human)
    Punkte_Mensch = Wahlanalyse(Wahlzahl_Human, Wahlzahl_PC)
    Punkte_PC = Wahlanalyse_Punkt_PC(Wahlzahl_Human, Wahlzahl_PC)

print("Entstand:")
print("\t" + str(Punkte_PC) + " Punkte für den PC")
print("\t" + str(Punkte_Mensch) + "Punkte für dich")
