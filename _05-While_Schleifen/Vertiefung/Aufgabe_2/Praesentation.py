import random

go = True


while go:
    #Zahleneingabe
    tipp_liste = []
    zahleingabe = True
    durchgaenge = 1
    while zahleingabe:
        tipp = input("Geben Sie Ihre Zahlen zwischen 1 und 49 ein: ")
        tipp_liste.append(tipp)
        durchgaenge += 1
        if durchgaenge == 7:
            zahleingabe = False


    #Ziehung
    ziehung_fortsetzen = 1
    ziehung_beginn = True
    gezogen_liste = []
    while ziehung_beginn:
        gezogenzahl = random.randint(1, 49)
        gezogen_liste.append(gezogenzahl)
        ziehung_fortsetzen += 1
        if ziehung_fortsetzen == 7:
            ziehung_beginn = False

    richtige = gezogen_liste.count(tipp_liste)
    print(richtige)
    exit()