# ----------------------------------------------------- Listen ---------------------------------------------------------
Vokabelliste = []


# --------------------------------------------------- Funktionen -------------------------------------------------------


def Auswahl_Aktionen_Überblick():
    auswahl_aktion = Hauptmenü()
    print("\n")
    if auswahl_aktion == 1:  # Neue Vokabeln eingeben
        anlegen = neue_Vok_anlegen()
        print("\n")
        Menü = Auswahl_Aktionen_Überblick()
    elif auswahl_aktion == 2:  # Abfrage starten
        abfrage = Abfrage()
        print("\n")
        Menü = Auswahl_Aktionen_Überblick()
    elif auswahl_aktion == 3:  # Zwischenstand anzeigen
        zwischenstand_anzeigen = Zwischenstand()
        print("\n")
        exit()
        Menü = Auswahl_Aktionen_Überblick()
    elif auswahl_aktion == 4:  # Programm verlassen
        print("Ich hoffe, du hattest Spaß mit meinem Vokabeltrainer!")
        print("Hoffentlich sehen wir uns bei der nächsten Abfrage wieder.")
        exit()
    print(Vokabelliste)
    exit()


def Hauptmenü():
    print("\t(1) Neue Vokabeln anlegen")
    print("\t(2) Vokabeln Abfragen")
    print("\t(3) Zwischenstand anzeigen")
    print("\t(4) Vokabeltrainer verlassen")
    auswahl = int(input("\tBitte gebe hier die Nummer deiner Wahl ein: "))
    return auswahl


def Abfrage():
    for Vokabeln in Vokabelliste:
        antwort = input("Was bedeutet '" + Vokabeln[0] + "' im Englischen? ")
        if antwort == Vokabeln[1]:
            print("Super! Das war richtig")
            Vokabeln[2] = int(Vokabeln[2]) + 1
        else:
            print("Schade, das war leider falsch! Die Übersetzung von '" + Vokabeln[0] + "' ins Englische wäre '" + Vokabeln[1] + "' gewesen.")
            trotzdem_gelten = input("Möchtest du deine Antwort trotzdem gelten lassen? (Ja/Nein) ")
            if trotzdem_gelten == "Ja":
                print("Die Antwort wird trotzdem gelten gelasen!")
                Vokabeln[2] = int(Vokabeln[2]) + 1
            else:
                print("0k, die Antwort gilt nicht!")


def neue_Vok_anlegen():
    anlegen = True
    while anlegen:
        Vokabel = []
        Bedeutung_D = input("Bitte gebe hier zunächst die deutsche Bedeutung der Vokabel ein: ")
        Vokabel.append(Bedeutung_D)
        Bedeutung_E = input("Gebe nun hier ein, was diese Vokabel im Englischen bedeutet: ")
        Vokabel.append(Bedeutung_E)
        Vokabel.append(str(0))
        Vokabelliste.append(Vokabel)
        weiter_anlegen = input("Möchtest du eine weitere Vokabel anlegen oder zurück ins Hauptmenü ('Ja' = weitere "
                               "Vokabel, 'Nein' = zurück ins Hauptmenü)? ")
        if weiter_anlegen == "Ja":
            print("Ok, wir beginnen nun mit dem Anlegen der nächsten Vokabel")
        elif weiter_anlegen == "Nein":
            anlegen = False


def Zwischenstand():
    print("Deutsch\t\t\tEnglisch\t\t\tAnzahl richtiger Versuche")
    print("-------------------------------------------------------------")
    for zwischenstand in Vokabelliste:
        print(str(zwischenstand[0]) + "\t\t\t" + str(zwischenstand[1]) + "\t\t\t\t" + str(zwischenstand[2]))
    print("\n")
    Menü = Auswahl_Aktionen_Überblick()
# --------------------------------------------------- Hauptteil -------------------------------------------------------


print("\tWas möchtest du heute tun?")
Programm = Auswahl_Aktionen_Überblick()

