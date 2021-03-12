def fx(x):
    x = x + "x"
    return x

x = fx("")
while len(x) < 10:
    print(x)
    x = fx(x)
print("ausge-x-t: " + x)