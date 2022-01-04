from collections import Counter


def number_of_pairs(gloves):
    return sum(c // 2 for c in Counter(gloves).values())


# Sample w/ 2 pairs found
input = ["red", "green", "red", "blue", "blue"]
print("Input: {0}\nNumber of Pairs: {1}".format(input, number_of_pairs(input)))
assert number_of_pairs(input) == 2  # Simple Unit Tests

from collections import Counter

def score(dice):
    score = 0
    scores = {
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200
    }
    special_scores = {1: 100, 5:50}
    for k in Counter(dice).items():
        if k[0] == 1 or k[0] == 5:
            score += ((k[1] // 3) * scores[k[0]]) + ((k[1] % 3) * special_scores[k[0]])
    return score
