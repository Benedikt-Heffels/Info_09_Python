quiz = [["Berlin", "Deutschland"], ["London", "Großbritannien"], ["Paris", "Frankreich"], ["Madrid", "Spanien"]]


punkte = 0
for frage in quiz:
    antwort = input("Wie heißt die Hauptstadt von " + frage[1] + "? ")
    if antwort == frage[0]:
        print("Super, das war richtig!")
        punkte += 1
    else:
        print("Schade! " + frage[0] + " ist die Hauptstadt von " + frage[1] + ".")
print("Du hast " + str(punkte) + " von " + str(len(quiz)) + " Fragen richtig beantwortet!")
