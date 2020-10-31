a = []
b = []

f = 16
g = 58

fi = 11
gi = 50

for i in range(1000):
    a.append(f+(fi*i))
    b.append(g+(gi*i))

for i in a:
    for j in b:
        if i == j and i/fi > 50:
            print(i)
