waren = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier", "Milch"]
print("Willkommen bei Bauer Hampel!")
name = input("Geben Sie bitte Ihren Namen ein: ")
print("Hallo, " + name + "!")
print("Unser Angebot heute:" + str(waren))
wahl = input("Was darf's denn sein? ")

if wahl in waren:
    print("Gerne! Hier sind Ihre " + wahl)
else:
    print("Schade! " + wahl + " haben wir heute leider nicht.")

teilnahme = input("Möchten Sie an unserem Gewinnspiel teilnehmen? (Ja/Nein) ")
if teilnahme == "Ja":
    print("Sehr schön! Hier die Schätzfrage: ")
    anzahl_eier = 16
    tipp = input("Wie viele Eier haben unsere Hennen heute Morgen produziert?")

    if tipp == "16":
        print("Herzlichen Glückwunsch! Sie haben einen Gutschein über 5 € gewonnen.")
    elif int(tipp) > 10 or int(tipp) < 20:
        print("Schade, Sie waren ganz nah dran!")
    else:
        print("Schade, vielleicht haben Sie beim nächsten Mal mehr Glück!")
elif teilnahme == "Nein":
    print("Schade, vielleicht beim nächsten Mal.")
else:
    print("Ihre Antwort habe ich leider nicht verstanden.")