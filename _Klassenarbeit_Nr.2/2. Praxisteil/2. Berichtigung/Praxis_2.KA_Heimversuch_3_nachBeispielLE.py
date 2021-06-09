import random

def benutzereingabe():
    print("Ein sicheres Passwort hat zwischen 8 und 20 Zeichen. Wie lang soll ihr Passwort sein?")
    gewuenschte_laenge_pw = int(input("Bitte geben sie ihre Wahl hier ein: "))
    falsche_eingabe = True
    while falsche_eingabe:
        if gewuenschte_laenge_pw < 8 or gewuenschte_laenge_pw > 20:
            print("Ihre Eingabe wird nicht akzeptiert, da ein so kurzes Passwort unsicher wäre oder"
                  " ein so langes Passwort nicht merkbar wäre bzw. nicht akzeptiert wird.")
            gewuenschte_laenge_pw = int(input("Bitte geben sie hier eine neue Passwortlänge ein: "))
        else:
            falsche_eingabe = False
    return gewuenschte_laenge_pw

def moegliche_zeichen():
    liste_moegliche_zeichen = ["!", "$", "?", "%", "#"]
    for moegliches_zeichen in range (0, 10):
        liste_moegliche_zeichen.append(moegliches_zeichen)
    return liste_moegliche_zeichen

def passwort_erstellung():
    passwort = ""
    soll_laenge_pw = benutzereingabe() - 1
    derzeitige_laenge_pw = 0
    anzahl_zeichen = len(moegliche_zeichen()) - 1
    while derzeitige_laenge_pw < soll_laenge_pw:
        zeichen = random.randint(0, anzahl_zeichen)
        zeichen_endgueltig = str(moegliche_zeichen()[zeichen])
        passwort += zeichen_endgueltig
        derzeitige_laenge_pw += 1
    print("\n\nIhr sicheres und zufällig erstellte Passwort:")
    return passwort


print(passwort_erstellung())