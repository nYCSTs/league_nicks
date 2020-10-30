def mdc(num_a, num_b):
    da = divisors(num_a)
    db = divisors(num_b)
    results = []

    for i in da:
        for j in db:
            if i == j:
                results.append(i)
    if len(results) == 0:
        return 1
    return results[-1]


def divisors(num):
    d = []
    for i in range(num + 1)[1:]:
        if num % i == 0:
            d.append(i)
    return d


def multiples(num):
    mult = []
    for i in range(100)[1:]:
        mult.append(num*i)
    return mult


def mmc(num_a, num_b):
    ma = multiples(num_a)
    mb = multiples(num_b)

    for i in ma:
        for j in mb:
            if i == j:
                return i
