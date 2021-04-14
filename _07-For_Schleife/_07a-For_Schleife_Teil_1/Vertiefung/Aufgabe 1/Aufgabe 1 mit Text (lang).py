
def Auswahl_inex (wahl, Ende):
    if wahl == "Inklusive":
        Ende_neu = Ende + 1
    elif wahl == "Exklusive":
        Ende_neu = Ende
    return Ende_neu

def Auswahl_Erklaer (wahl, Ende):
    if wahl == "Erklärung":
        print("Inklusive bedeutet, dass der Wert, denn sie als Ende eingegeben haben, auch in der Liste auftaucht.")
        print("Exklusive bedeutet, dass dieser Wert nicht in der Liste auftaucht.")
        inex_Ende_ohne_Erklaerung = input("Soll das Ende inklusive oder exklusive genommen werden? ('Inklusive'/'Exklusive')")
        Auswahl_inex(inex_Ende_ohne_Erklaerung, Ende)


# def Hauptmenü (wahl, Ende):
#     if wahl == "Inklusive":
#         Ende_neu = Ende + 1
#     elif wahl == "Exklusive":
#         Ende_neu = Ende
#     elif wahl == "Erklärung":
#         print("Inklusive bedeutet, dass der Wert, denn sie als Ende eingegeben haben, auch in der Liste auftaucht.")
#         print("Exklusive bedeutet, dass dieser Wert nicht in der Liste auftaucht.")
#         inex_Ende_ohne_Erklaerung = input("Soll das Ende inklusive oder exklusive genommen werden? ('Inklusive'/'Exklusive')")
#         Hauptmenü (inex_Ende_ohne_Erklaerung, Ende)
#     return Ende_neu


Beginn = int(input("Bei welcher Zahl soll das Programm beginnen?"))
Ende = int(input("Bei welcher Zahl soll das Programm Enden? "))
inex_Ende = input("Soll das Ende inklusive oder exklusive genommen werden? ('Inklusive'/'Exklusive'/'Erklärung' für eine Erklärung der beiden Wörter)")

main_Ende_neu = Auswahl_Erklaer(inex_Ende, Ende)
main_Ende_neu = main_Ende_neu


for x in range(Beginn, main_Ende_neu):
    print(x)