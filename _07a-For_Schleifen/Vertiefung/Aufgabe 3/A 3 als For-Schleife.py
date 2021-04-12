x = int(input("Eine Zahl Bitte!:"))
i = 1

for i in range(1001):
    if i % x == 0:
        print(i)