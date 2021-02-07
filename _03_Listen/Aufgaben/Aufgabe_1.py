# Wir legen eine Liste an
liste = ["Banane", "Erdbeere", "Apfel", "Kiwi", "Apfel"]
print(liste)

print("_____________________________________________________________")

l = len(liste)
print(l)
print("Die Liste enthält " + str(l) + " Elemente!")

print("_____________________________________________________________")

print(liste.count("Apfel"))
print(liste.count("Banane"))


print("_____________________________________________________________")

print(liste[-1])
print(liste[-2])
print(liste[-3])
print(liste[-4])

 
print("_____________________________________________________________")

print(liste.index("Erdbeere"))
idx = liste.index("Kiwi")
print(idx)
print(type(idx))

print("_____________________________________________________________")

liste[0] = "Birne"
print(liste)

print("_____________________________________________________________")

liste2 = ["Haselnuss", "Walnuss", "Mandel"]
liste.extend(liste2)
print(liste)


print("_____________________________________________________________")

liste.sort()
print(liste)

print("_____________________________________________________________")

liste.pop(3)
print(liste)


print("_____________________________________________________________")

leere_liste = []
print(leere_liste)
print(type(leere_liste))
print(len(leere_liste))


print("_____________________________________________________________")


print("_____________________________________________________________")



print("_____________________________________________________________")



print("_____________________________________________________________")
leere_liste = []
print(leere_liste)
print(len(leere_liste))


