def funktion_a():
    print("Hallo! Ich bin Funktion A!")
    funktion_b()
def funktion_b():
    print("Hallo! Ich bin Funktion B!")

# hier fängt der Hauptteil an
print("Anfang")
funktion_a()
print("\nMitte")
funktion_b()
print("\nEnde")


#Es wird wieder eine neue Funktion erstellt. Am Ende von Funktion A wird noch Funktion B ausgegeben.