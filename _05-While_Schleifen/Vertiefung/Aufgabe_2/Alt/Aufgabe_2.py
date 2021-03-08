import random

print("Hallo! Willkommen bei Lotto Ben. Bei diesem Spiel müssen sie 6 Zahlen Tippen.")
Start = input("Wollen sie fortfahren? ")
if Start == "Ja":
    go = True
else:
    go = False

while go == True:
    zahl1 = input("Bitte geben sie ihre erste Zahl ein: ")
    zahl2 = input("Bitte geben sie ihre zweite Zahl ein: ")
    zahl3 = input("Bitte geben sie ihre dritte Zahl ein: ")
    zahl4 = input("Bitte geben sie ihre vierte Zahl ein: ")
    zahl5 = input("Bitte geben sie ihre fünfte Zahl ein: ")
    zahl6 = input("Bitte geben sie ihre sechste Zahl ein: ")
    print("Wir ziehen nun die Lottozahlen!")
    retry = True
    # lösung1 = random.randint(0, 49)
    # lösung2 = random.randint(0, 49)
    # lösung3 = random.randint(0, 49)
    # lösung4 = random.randint(0, 49)
    # lösung5 = random.randint(0, 49)
    # lösung6 = random.randint(0, 49)
    #
    # if lösung1 == lösung2 or lösung3 or lösung4 or lösung5 or lösung6:
    #     retry = True
    # else:
    #     if lösung2 == lösung3 or lösung4 or lösung5 or lösung6:
    #         retry = True
    #     else:
    #         if lösung3 == lösung4 or lösung5 or lösung6:
    #             retry = True
    #         else:
    #             if lösung4 == lösung5 or lösung6:
    #                 retry = True
    #             else:
    #                 if lösung5 == lösung6:
    #                     retry = True

    while retry == True:
        lösung1 = random.randint(0, 49)
        lösung2 = random.randint(0, 49)
        lösung3 = random.randint(0, 49)
        lösung4 = random.randint(0, 49)
        lösung5 = random.randint(0, 49)
        lösung6 = random.randint(0, 49)
        lösungen = [lösung1, lösung2, lösung3, lösung4, lösung5, lösung6]

        if lösung1 == lösung2 or lösung3 or lösung4 or lösung5 or lösung6:
            retry = True
        else:
            if lösung2 == lösung3 or lösung4 or lösung5 or lösung6:
                retry = True
            else:
                if lösung3 == lösung4 or lösung5 or lösung6:
                    retry = True
                else:
                    if lösung4 == lösung5 or lösung6:
                        retry = True
                    else:
                        if lösung5 == lösung6:
                            retry = True

    print("Das sind die sechs gezogenen Zahlen: ", lösung1, lösung2, lösung3, lösung4, lösung5, lösung6)


    Start = input("Wollen sie fortfahren? ")
    if Start != "Ja":
        go = False

print("Schade! Vielleicht besuchen sie uns demnächst ja nochmal. ")
