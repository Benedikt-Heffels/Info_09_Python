import random
# Benedikt Heffels

passwort = []
Sonderzeichen = ["#", "!", "?", "%", "$"]
print("Willkommen beim Passwortgenerator!")
print("Wie lange soll ihr Passwort sein? Es muß mindestens 8 und maximal 20 Zeichen enthalten!")
anzahl_zahlen_passwort = input("Ihre Eingabe bitte: ")
anzahl_zahlen_passwort_int = anzahl_zahlen_passwort

for x in anzahl_zahlen_passwort_int:
    zufallszahl_passwort = random.randint(0, 10)
    # zufallszahl_passwort_str = str(zufallszahl_passwort)
    passwort.append(zufallszahl_passwort)


# anzahl_sonderzeichen = anzahl_zahlen_passwort_int/4
# anzahl_sonderzeichen_int = 4 # int(anzahl_sonderzeichen)
anzahl_sonderzeichen = int(4)


# länge_passwort = len(passwort)
# for y in anzahl_sonderzeichen:
#     position_sonderzeichen = random.randint(0, länge_passwort)
#     zufälliges_sonderzeichen = random.randint(0, 4)
#     passwort.insert(position_sonderzeichen, Sonderzeichen[zufälliges_sonderzeichen])

print(passwort)



