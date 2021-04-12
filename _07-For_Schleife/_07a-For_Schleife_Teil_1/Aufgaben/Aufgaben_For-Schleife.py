bereich1 = list(range(10))
print(bereich1)
#Erstellt eine Liste mit allen Zahlen von 0 bis (exklusive) 10.
#Die 10 nennt die obere Grenze der Zahlen. Es wird bei 0 zu Zählen begonnen

bereich2 = list(range(1, 10))
print(bereich2)
#Erstellt eine Liste mit allen Zahlen zwischen 1 und (exklusive) 10

bereich3 = list(range(1, 10, 2))
print(bereich3)
#Erstellt eine Liste mit allen Zahlen unter 10. Die Zahlen werden +2 gerechnet (2er Schritte).

bereich4 = list(range(10, 1, -1))
print(bereich4)
#Erstellt rückwärts eine Liste mit allen Zahlen unter 10

print("________________________________________________________________")

for x in range(0, 10):
    print(x)
# Während x zwischen 0 und 10 liegt, drucke x

print("________________________________________________________________")

for x in range(0, 10, 2):
    print(x)
#Während x zwischen 0 und 10 liegt, drucke x. Die letzte Zahl sorgt jedoch dafür, dass nur jede zweite Zahl ausgegeben wird.

print("________________________________________________________________")

for x in range(10, 0, -1):
    print(x)
#Das -1 sorgt dafür, dass die Zahlen runtergezählt werden. Dannach werden alle Zahlen zwischen 10 und 0 ausgegeben.
