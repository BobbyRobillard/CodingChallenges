def invert(s):
    inv = "".join(["1" if substr == "0" else "0" for substr in s])
    print("Inversion of {} is: {}".format(s, inv))
    return inv


def solution(n, k):
    s = ["0"]
    for i in range(1, n):
        new_str = s[i - 1] + "1" + invert(s[i - 1])[::-1]
        print("NEW: " + new_str)
        s.append(new_str)
    s = "".join(s)
    print("STRING: {0}, K Pos: {1}".format(s, s[k - 1]))


solution(3, 1)
