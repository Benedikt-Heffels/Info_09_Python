waren = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier", "Milch"]
menge = [4, 1, 6, 10, 2, 0]

wahl = input("Was wollen sie haben? ")
zahl = int(waren.index(wahl))
print(zahl)
print(menge[zahl])