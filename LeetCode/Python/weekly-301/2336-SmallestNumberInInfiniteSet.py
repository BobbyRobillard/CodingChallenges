class SmallestInfiniteSet:

    def __init__(self):
        self.inf_set = set()

    def popSmallest(self) -> int:
        return self.inf_set.pop() if self.inf_set else None

    def addBack(self, num: int) -> None:
        self.inf_set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)