# Basic hash-map looking for ancestors
class TreeAncestor:

    def __init__(self, n: int, parents: list[int]):
        self.ancestors = {0: []}
        self.n = {}
        for i in range(1, len(parents)):
            self.ancestors[i] = [parents[i]] + self.ancestors[parents[i]]

    def getKthAncestor(self, node: int, k: int) -> int:
        return self.ancestors[node][k-1] if k <= len(self.ancestors[node]) else -1


# Binary lifting technique
class TreeAncestor:

    step = 15
    def __init__(self, n, A):
        A = dict(enumerate(A))
        jump = [A]
        for s in range(self.step):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            jump.append(B)
            A = B
        self.jump = jump

    def getKthAncestor(self, x, k):
        step = self.step
        while k > 0 and x > -1:
            if k >= 1 << step:
                x = self.jump[step].get(x, -1)
                k -= 1 << step
            else:
                step -= 1
        return x