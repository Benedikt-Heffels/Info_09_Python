spielfeld = [["111", "XX", "XXX"], ["XXX", "XXX", "XXX"], ["ÜÜÜÜ", "vvv", "kkk"]]
spielfeld_leer = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(spielfeld)

for falsches_element in spielfeld:
    falsches_element.clear()
    falsches_element = "1"

print(spielfeld)
spielfeld[0][0] = "1.1"
print(spielfeld)
