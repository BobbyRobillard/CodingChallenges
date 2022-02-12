def solution(n):
    n = str(n)
    if len(n) % 2 != 0: return False
    n = list(n)
    a,b = n[:len(n)//2], n[len(n)//2:]
    a,b = list(map(int, a)), list(map(int, b))
    return sum(a) == sum(b)
