from math import log

# FIRST CORRECT SOLUTION #
def compare_powers(n1, n2):
    if n1[0] == n2[0] and n1[0] == 1:
        return 0

    if n1[0] == n2[0]:
        return 1 if n2[1] > n1[1] else (-1 if n1[1] > n2[1] else 0)

    if n1[1] == n2[1]:
        return 1 if n2[0] > n1[0] else (-1 if n1[0] > n2[0] else 0)

    res1 = log(n1[0]) * n1[1]
    res2 = log(n2[0]) * n2[1]
    return 1 if res2 > res1 else (-1 if res1 > res2 else 0)


# REFACTORED SOLUTION #
def compare_powers(n1, n2):
    res1 = log(n1[0]) * n1[1]
    res2 = log(n2[0]) * n2[1]
    return 1 if res2 > res1 else (-1 if res1 > res2 else 0)


# EXAMPLE AND TESTING #
print(
    "\nInput: {0} | Compare Powers: {1}".format(
        "[1, 7], [1, 8]", compare_powers([1, 7], [1, 8])
    )
)

assert compare_powers([1, 7], [1, 8]) == 0  # Simple Unit Tests
assert compare_powers([3, 7], [2, 8]) == -1  # Simple Unit Tests
