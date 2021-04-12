def funktion_a():
    print("Hallo! Ich bin Funktion A!")
    funktion_b()
def funktion_b():
    print("Hallo! Ich bin Funktion _07b-For_Schleife_Teil_2!")
    funktion_a()

# hier fängt der Hauptteil an
print("Anfang")
funktion_a()
print("\nMitte")
funktion_b()
print("\nEnde")


#Es werden eine Millionen Fehler ausgegeben, die durch funktion_a() verursacht werden#
#RecursionError -> Das Programm würde sich nur wiederholen, das Heisst es würde unendlich mal die beiden Funktionen ausgeben. Das läst Python jedoch nicht zu.