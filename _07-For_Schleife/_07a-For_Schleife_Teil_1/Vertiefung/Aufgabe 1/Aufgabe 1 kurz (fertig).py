# ------Hauptteil-------
print("Hallo, Willkommen bei diesem Programm!")
Anfang = int(input("Bitte geben sie den Anfangswert ein: "))
Ende = int(input("Bitte geben Sie den Endwert ein: "))

y = 0
for x in range(Anfang, Ende):
    print(x)
    y = y +x


print(y)


