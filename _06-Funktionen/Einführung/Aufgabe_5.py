def funktion(x, y):
    print("Hallo! Meine Parameter sind: " + str(x) + " und " + str(y))
    z = x * y
    return z

# hier fängt der Hauptteil an
print("Anfang")

ergebnis = funktion(3, 8) # In die Funktion werden bei x und y die Zahlen 3 und 8 eingesetzt. Zudem werden die Parameter
                          # im Satz mit print ausgedruckt. Die return (=24) wird als Variable Ergebnis gespeichert
print("\nErgebnis = " + str(ergebnis)) #Es wird die Variable 'ergebnis' ausgegeben. In ihr Stand die Funktion.
                                       # Es wurde jedoch nur z gesspeichert, welches hier als Ergebnis ausgegeben wird.

print("\nEnde")