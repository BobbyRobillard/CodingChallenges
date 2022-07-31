nums = [2, 5, 6, 8]
# While every item is not a 1 or 0, mod 2 it
while True:
    nums = [item % 2 for item in nums]
    if all(x == 0 for x in nums) or all(x == 1 for x in nums):
        print("yes")
        break
    if 0 in nums and 1 in nums and all(x < 2 for x in nums):
        print("no")
        break



