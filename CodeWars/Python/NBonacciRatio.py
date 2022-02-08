def n_bonacci_value(n, x):
    bonaccis = [0, 1]
    for i in range(2, x + 1):  # Fib w/o recursion
        bonaccis.append(n * bonaccis[-1] + bonaccis[-2])
    return bonaccis[x - 1]


def n_bonacci_ratio(n):
    res1 = n_bonacci_value(n, 100)
    res2 = n_bonacci_value(n, 99)
    return float("{0:.8f}".format(res1 / res2))


print("N Bonacci Ratio of N=1 | {0}".format(str(n_bonacci_ratio(1))))
print("N Bonacci Ratio of N=2 | {0}".format(str(n_bonacci_ratio(2))))
