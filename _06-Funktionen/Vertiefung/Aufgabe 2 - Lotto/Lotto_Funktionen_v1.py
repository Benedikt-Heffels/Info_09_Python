import random

#Listen für Ja und Nein
Ja = ["Ja", "JA", "ja", "j", "J", "yes", "Y"]
Nein = ["Nein", "NEIN", "nein", "n", "N", "no"]


#Funktionen zur Eingabe der Tipps
def eingabe_kontrolleV1(eingabe_zahl):
    if eingabe_zahl in eingabe_liste or eingabe_zahl <= 0 or eingabe_zahl >= 49:
        eingabe_zahl_weiterer_Versuch = int(input("Bitte geben Sie ihre Zahl Nummer "  + str(len(eingabe_liste) + 1) + " erneut ein. "
                                                  "Beachten sie, dass diese Zahl zwischen 1 und 49 liegen muss und sie diese Zahl noch nicht getippt haben dürfen! "))
        eingabe_kontrolleV2(eingabe_zahl_weiterer_Versuch)
    else:
        eingabe_liste.append(eingabe_zahl)


def eingabe_kontrolleV2(eingabe_zahl_weiterer_Versuch):
    if eingabe_zahl_weiterer_Versuch in eingabe_liste or eingabe_zahl_weiterer_Versuch <= 0 or eingabe_zahl_weiterer_Versuch >= 49:
        eingabe_zahl_weiterer_Versuch = int(input("Bitte geben Sie ihre Zahl Nummer "  + str(len(eingabe_liste) + 1) + " erneut ein. "
                                                  "Beachten Sie, dass diese Zahl zwischen 1 und 49 liegen muss und Sie diese Zahl noch nicht getippt haben dürfen! "))
        eingabe_kontrolleV2(eingabe_zahl_weiterer_Versuch)
    else:
        eingabe_liste.append(eingabe_zahl_weiterer_Versuch)



#Ende der Schleife-Funktion
def Schleife_Ende(Liste):
    if len(Liste) == 6:
        Schleife_Beginnen = False
    else:
        Schleife_Beginnen = True
    return Schleife_Beginnen



# Richtige Lösungen Funktionen
def anzahl_richtige_Zaehlung(gezogen_liste, eingabe_liste):
    anzahl_richtige_liste = []
    position = 0
    while position <=5:
        if eingabe_liste[position] in gezogen_liste:
            anzahl_richtige_liste.append(eingabe_liste[position])
        position = position + 1
    anzahl_richtige = len(anzahl_richtige_liste)
    return anzahl_richtige


def richtige_loesungen_waeren_gewesen(richtige_liste):
    print("Die richtigen Zahlen wären " + str(richtige_liste) + " gewesen.")



#Weiterspiel-Funktionen
def neuer_Versuch():
    neue_Runde = input("Wollen Sie eine weitere Runde spielen und ihr Glück erhöhen? ")
    Spiel_Start(neue_Runde)


def Spiel_Start(neue_Runde):
    if neue_Runde in Ja:
        go = True
    elif neue_Runde in Nein:
        go = False
    else:
        go = False
    return go



# ------------- Beginn des Lottospieles -------------
print("Hallo! Willkommen bei Lotto Hückelhoven. Bei diesem Spiel müssen Sie 6 Zahlen Tippen.")
print("Die Zahlen müssen zwischen 1 und 49 liegen! Zudem dürfen sich die Zahlen in Ihren Tipps nicht wiederholen.")
Start = input("Wollen Sie fortfahren? ")

go = Spiel_Start(Start)

while go:
    # Man gibt seine Tips ein
    print(" ")
    Schleife_Beginnen = True
    eingabe_liste = []
    while Schleife_Beginnen == True:
        eingabe_zahl = int(input("Bitte geben Sie nun Ihre Zahl Nummer " + str(len(eingabe_liste) + 1) + " ein. Beachten Sie, "
                            "dass diese Zahl zwischen 1 und 49 liegen muss und, dass Sie diese Zahl noch nicht getippt haben! "))
        eingabe_kontrolleV1(eingabe_zahl)
        Schleife_Beginnen = Schleife_Ende(eingabe_liste)


    #Die richtigen Zahlen werden gezogen
    Schleife_Beginnen = True
    gezogen_liste = []
    while Schleife_Beginnen == True:
        gezogen_zahl = random.randint(1, 49)
        if gezogen_zahl not in gezogen_liste:
            gezogen_liste.append(gezogen_zahl)
        Schleife_Beginnen = Schleife_Ende(gezogen_liste)

    # Die liste der Tipps und der gezogenen Zahlen werden verglichen
    print(" ")
    anzahl_richtige = anzahl_richtige_Zaehlung(gezogen_liste, eingabe_liste)
    if anzahl_richtige == 6:
        print("Glückwunsch! Sie haben alle Zahlen richtig getippt. Das ist der Hauptgewinn.")
        go = neuer_Versuch()
    elif anzahl_richtige == 0:
        print("Leider haben Sie keine richtige Zahl getippt.")
        richtige_loesungen_waeren_gewesen(gezogen_liste)
        go = neuer_Versuch()
    else:
        print("Glückwunsch. Sie haben " + str(anzahl_richtige) + " Zahlen richtig getippt.")
        richtige_loesungen_waeren_gewesen(gezogen_liste)
        go = neuer_Versuch()

print("\n \nImpressum")
print("Lotto Hückelhoven Gmbh")
print("Benedikt Heffels, Luca Foerster und Fathi Kacar")
print("Irgendwo im Nirgendwo 1")
print("41836 Hückelhoven")


