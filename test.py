from functions import mdc, mmc, multiples

a = 10
b = 210


for i in range(1, 1000):
    for j in range(1, 1000):
        if mdc(i, j) == a and mmc(i, j) == b:
            print(i, j)
