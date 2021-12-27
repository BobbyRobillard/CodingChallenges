from collections import Counter

def number_of_pairs(gloves):
    return sum(c // 2 for c in Counter(gloves).values())

# Sample w/ 2 pairs found
input = ["red", "green", "red", "blue", "blue"]
print("Input: {0}\nNumber of Pairs: {1}".format(input, number_of_pairs(input)))
assert number_of_pairs(input) == 2 # Simple Unit Tests
