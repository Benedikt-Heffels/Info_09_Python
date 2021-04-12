# ------- Funktionen -------
def wahlkontrolle1 (wahl):
    if wahl in Liste_waehlbar:
        return wahl
    else:
        Benutzer_Wahl_2 = input("Tut mir Leid! Diese Umrechnungsart gibt es nicht. Bitte versuchen Sie es erneut")
        Benutzer_Wahl_2 = int(Benutzer_Wahl_2)


def wahlkontrolle2 (wahl2):
    if wahl2 in Liste_waehlbar:
        return wahl2
    else:
        Benutzer_Wahl_2 = input("Tut mir Leid! Diese Umrechnungsart gibt es nicht. Bitte versuchen Sie es erneut")
        Benutzer_Wahl_2 = int(Benutzer_Wahl_2)
        wahlkontrolle2(Benutzer_Wahl_2)


def Umrechnung (wahl, Temperatur):
    if wahl == 1:
        Ergebnis = Temperatur + 273.15
    elif wahl == 2:
        Ergebnis = Temperatur * (9/5) + 32
    elif wahl == 3:
        Ergebnis = Temperatur - 273.15
    elif wahl == 4:
        Ergebnis = (Temperatur - 273.15) * (9/5) + 32
    elif wahl == 5:
        Ergebnis = 5/9 * (Temperatur-32)
    elif wahl == 6:
        Ergebnis = (Temperatur - 32) / (9/5) + 273.15
    return Ergebnis


# -------- Listen ---------
Umrechnungsarten = [["Celsius", "nach", "Kelvin"], ["Celsius", "nach", "Fahrenheit"], ["Kelvin", "nach", "Celsius"],
                    ["Kelvin", "nach", "Fahrenheit"], ["Fahrenheit", "nach", "Celsius"], ["Fahrenheit", "nach", "Kelvin"]]
Liste_waehlbar = [1, 2, 3, 4, 5, 6]


# --------- Hauptteil --------
print("Willkommen beim Temperaturumwandler! Folgende Umrechnungsmöglichkeiten gibt es:")
print("\t(1) Umrechnung von", Umrechnungsarten[0])
print("\t(2) Umrechnung von", Umrechnungsarten[1])
print("\t(3) Umrechnung von", Umrechnungsarten[2])
print("\t(4) Umrechnung von", Umrechnungsarten[3])
print("\t(5) Umrechnung von", Umrechnungsarten[4])
print("\t(6) Umrechnung von", Umrechnungsarten[5])
Benutzer_Wahl = input("Welche dieser Umrechnungsarten möchten sie nutzen? Bitte geben sie dafür einfach dessen Nummer ein (z._07b-For_Schleife_Teil_2. 1)")
Benutzer_Wahl = int(Benutzer_Wahl)
#print(type(Benutzer_Wahl))
Benutzer_Wahl_edited = wahlkontrolle1(Benutzer_Wahl)
Benutzer_Wahl_edited = int(Benutzer_Wahl_edited)

Wahl_Position_und_Text_List = Umrechnungsarten[Benutzer_Wahl_edited]
print(type(Wahl_Position_und_Text_List))


# Benutzereingabe_Temperatur = input("Bitte geben sie nun die Temperatur ein, die sie von ", Wahl_Position_und_Text_List, " umrechnen wollen: ")
# Benutzereingabe_Temperatur = float(Benutzereingabe_Temperatur)
#
# Ergebnis_Umwandlung = Umrechnung(Benutzer_Wahl_edited, Benutzereingabe_Temperatur)
#
# print("Die Umwandlung ihrer Temperatur von ", Umrechnungsarten[Benutzer_Wahl_edited], " hat folgendes Ergebnis ergeben:")
# print("\n\t", Benutzereingabe_Temperatur, Umrechnungsarten[Benutzer_Wahl_edited][0], " sind",
#       Ergebnis_Umwandlung, Umrechnungsarten[Benutzer_Wahl_edited][2])



