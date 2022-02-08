import re

# Working Solution
# Runtime: 23ms on 20 item list.
# Memory: 12.2MB
def solution(string):
    return round(sum(map(float, re.findall(r"(\d+\.\d+|\d+)", string))), 2)

# ------------------------------------------------------------------------------

# Initial Thought
# Loop through entire string, building temp_price and adding to total when done
# Issue: Too many side cases to code in
# Passes 8/9 tests, issue with multiple decimal points
def solution_incomplete(string):
    total = 0
    next_price = ""
    for c in string:
        if c.isdigit() or (c == "." and c not in next_price):
            next_price += c
        else:
            print("NP:", next_price)
            if len(next_price) >= 1:
                try:
                    total += float(next_price)
                    next_price = ""
                except:
                    next_price = ""

    if len(next_price) > 1:
        total += float(next_price)

    return total

# ------------------------------------------------------------------------------
from HelperFunctions import get_memory_used

# Currently only testing 1 large input.
# Uncomment the rest or add yours to the end to test an input
tests = [
    "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4",
    # "blue suit for 24$, cape for 12.99$ & glasses for 15.70",
    # "wanna 22.2&15.3olo 0.00 and 12.12kk0.02 ..34",
    # "Each snack for 2.21$, each drink for 1.1"
]

for t in tests:
    print("TESTING:", t, "\nRESULT:" , str(solution(t)))

get_memory_used()
