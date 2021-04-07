#----------- Funktionen -------------
def wahlkontrolle_v1 (wahl):
    if wahl in liste_waehlbar:
        #print("ok")
        return int(wahl)
    else:
        wahlkontrolle_korrektur(wahl)
        #return wahl


def wahlkontrolle_korrektur(eingabe_wahl_k):
    eingabe_wahl_k = int(input("Bitte versuchen sie erneut eine Zahl einzugeben!"))
    if eingabe_wahl_k in liste_waehlbar:
        print("ok")
        return eingabe_wahl_k
    else:
        wahlkontrolle_korrektur(eingabe_wahl_k)


# ----------- Listen ----------------
Umrechnungsarten = ["Celsius nach Kelvin", "Celsius nach Fahrenheit", "Kelvin nach Celsius", "Kelvin nach Fahrenheit",
                    "Fahrenheit nach Celsius", "Fahrenheit nach Kelvin"]
liste_waehlbar = [1, 2, 3, 4, 5, 6]
Umrechnungsformel = []
#------------ Hauptteil --------------
print("Willkommen beim Benschen Temperaturumwandler!")

print("Um fortfahren zu können, müssen wir zunächst wissen, welche Temperaturen sie umwandeln möchten!")
print("\t(1)", Umrechnungsarten[0])
print("\t(2)", Umrechnungsarten[1])
print("\t(3)", Umrechnungsarten[2])
print("\t(4)", Umrechnungsarten[3])
print("\t(5)", Umrechnungsarten[4])
print("\t(6)", Umrechnungsarten[5])
Umrechnungs_Wahl = int(input("Bitte geben sie die Nummer der Umrechnungsrichtung ein, die sie verwenden möchten"))
Umrechnungs_Wahl = wahlkontrolle_v1(Umrechnungs_Wahl)
Umrechnungs_Position_List = int(Umrechnungs_Wahl) - int(1)
print(type(Umrechnungs_Position_List))
#Umrechnungs_Wahl = int(Umrechnungs_Wahl)

temperatur_eingabe = input("Bitte geben sie die Temperatur ein, die sie von " + Umrechnungsarten[Umrechnungs_Position_List] + "umrechnen wollen")




#print(wahlkontrolle_v1(Umrechnungs_Wahl))