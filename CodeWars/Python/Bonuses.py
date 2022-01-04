import numpy as np

def bonus(arr, total):
    eqs = [
        [arr[0], arr[1], arr[2]],
        [arr[0], -1*arr[1], 0],
        [0, arr[1], -1*arr[2]],
    ]
    A = np.array(eqs)
    B = np.array([total, 0, 0])
    res = np.linalg.solve(A, B)
    new = []
    for i in range(0, 3):
        new.append(int(res[i]) * arr[i])
    return new


# EXAMPLE AND TESTING #
print("\nInput: {0}\nBonuses: {1}".format("[22, 3, 15]", bonus([22, 3, 15], 18228)))

assert bonus([22, 3, 15], 18228) == [1860, 13840, 2728]  # Simple Unit Tests
