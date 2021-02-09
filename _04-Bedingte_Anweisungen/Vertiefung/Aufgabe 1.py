waren = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier", "Milch"]
menge = [4, 1, 6, 10, 2, 0]
JA = ["Ja", "ja", "JA", "OK", "Ok", "ok"]
NEIN = ["Nein", "NEIN", "nein"]


print("Willkommen bei Bauer Hampel!")
name = input("Geben Sie bitte Ihren Namen ein: ")
print("Hallo " + name + "!")
print("Unser Angebot heute:" + str(waren))
wahl = input("Was darf's denn sein? ")

if wahl in waren:
    Gewuenschte_Anzahl = input("Gerne! Wie viele " + str(wahl) + " möchten sie denn? ")
    Nummer_waren = waren.index(wahl)
    if int(Gewuenschte_Anzahl) <= menge[Nummer_waren]:
        print("Gerne! Hier sind ihre ", Gewuenschte_Anzahl, wahl,  ".")
    elif int(Gewuenschte_Anzahl) >= int(menge[Nummer_waren]):
        print("Tut mir Leid! Wir haben leider nur ", str(menge[Nummer_waren]), str(wahl), " auf Lager!")
        print("Wollen sie den die restlichen ", int(Gewuenschte_Anzahl) - int(menge[Nummer_waren]), wahl, " vorbestellen?")
        Vorbestellung = input("Diese wären dann Morgen zur Abholung bereit! ")
        if Vorbestellung in JA:
            print("Gerne! Holen sie dann bitte morgen ihre restlichen ",  int(Gewuenschte_Anzahl) - int(menge[Nummer_waren]), wahl,  " ab.")
            print("Wollen sie denn die vorhandenen", str(menge[Nummer_waren]), str(wahl), "kaufen? ")
            Trostkauf = input("Sie würden diese dann jetzt bekommen! ")
            if Trostkauf in JA:
                print("Gerne! Hier sind ihre", str(menge[Nummer_waren]), str(wahl), ".")
            elif Trostkauf in NEIN:
                print("Das tut uns Leid! Dann können wir leider nichts für sie tun.")
        elif Vorbestellung in NEIN:
            print("Wollen sie denn die vorhandenen", str(menge[Nummer_waren]), str(wahl), "kaufen? ")
            Trostkauf = input("Sie würden diese dann jetzt bekommen! ")
            if Trostkauf in JA:
                print("Gerne! Hier sind ihre", str(menge[Nummer_waren]), str(wahl), ".")
            elif Trostkauf in NEIN:
                print("Das tut uns Leid! Dann können wir leider nichts für sie tun.")
else:
    print("Das habe ich leider nicht verstanden!")