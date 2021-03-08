import random

go = True
while go:
    x = random.randint(1, 6)
    print("Du hast eine " + str(x) + " gewürfelt!")

    txt = input("Nochmal würfeln? (Ja|Nein)")
    if txt != "Ja":
        go = False
print("Tschüss!")