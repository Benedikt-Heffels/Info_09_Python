import random

sonderzeichen = ["!", "$", "%", "#", "?"]
passwort = []


def passwort_zufaellig_erstellen():
    global gewuenschte_laenge_pw
    element_x = 0
    while element_x < gewuenschte_laenge_pw:
        zufallszahl = random.randint(0, 10)
        passwort.append(zufallszahl)
        element_x += 1
    element_y = 0
    while element_y < 3:
        position_sonderzeichen = random.randint(0, gewuenschte_laenge_pw)
        position_sonderzeichen_wert = position_sonderzeichen - 1
        art_sonderzeichen = random.randint(0, 4)
        passwort.pop(position_sonderzeichen_wert)
        passwort.insert(position_sonderzeichen_wert, sonderzeichen[art_sonderzeichen])
        element_y += 1


def willkommen_und_laenge_pw():
    global gewuenschte_laenge_pw
    print("Herzlich Willkommen beim sicheren Passwortgenerator!")
    falsches_passwort = False
    while not falsches_passwort:
        print("Ein sicheres Passwort hat zwischen 7 und 20 Zeichen. Bitte wählen sie aus, wie lang ihr Passwort sein "
              "soll!")
        gewuenschte_laenge_pw = int(input("Hier eingeben: "))
        if gewuenschte_laenge_pw <= 20 and gewuenschte_laenge_pw >= 8:
            falsches_passwort = True
        else:
            print("Falsche Eingabe!")


willkommen_und_laenge_pw()
passwort_zufaellig_erstellen()
print("\n\nIhr zufällig erstelltes und sicheres Passwort:")
print(passwort)

print("\n\nZur Sicherheit ist ihr Passwort hier nicht direkt sichtbar. Sie müssen nach oben scrollen!\n"
      "Ein paar Tipps zum Passwortmanagement:\n"
      "\t1. Schreiben sie sich das Passwort nicht offen sichtbar auf. Nutzen sie stattdessen eher einen Passwortmaneger!\n"
      "\t2. Verraten sie ihr Passwort niemanden\n"
      "\t3. Verwenden sie für verschiedene Dienste unterschiedliche Passwörter!\n"
      "...Und ihre Daten sind sicher!")
