x = int(input("Eine Zahl bitte:"))
y = 1
l = []

if x <= 1000:
    while 2 * y < x:
        if x % y <= 0:
            l.append(y)
        y = y + 1
    l.append(x)
    print(l)
