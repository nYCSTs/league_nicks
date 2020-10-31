def euclides(x, y):
    resto = 1
    results = []

    if(x >= y):
        while(resto != 0):
            results.append(int(x/y))
            resto = x % y
            x = y
            y = resto
    print(results)
