# -----------------------------------------------------------------------------
# CodeSignal Company Problem - Instacart - DeliveryFee
# https://app.codesignal.com/company-challenges/instacart/46cSk3fYxmzAs8dPJ

# RUNTIME: 40-44ms
# MEMORY USED: 12.3MB
# -----------------------------------------------------------------------------

def solution(intervals, fees, deliveries):
    intervals.append(24) # Added to make life simpler when filtering

    # For each interval, get the amount of items in it
    items_per_interval = [list(filter(lambda x: x[0] >= intervals[i] and x[0] < intervals[i+1], deliveries)) for i in range(len(intervals))]
    del items_per_interval[len(items_per_interval) - 1] # Remove extra item at end, since no items will be past 24

    # For each fee, find the ratio of the fee to the number of items
    ratio_to_maintain = -1
    for i, fee in enumerate(fees):
        if fee == 0:
            return False
        new_ratio = len(items_per_interval[i]) / fee
        if ratio_to_maintain < 0:
            ratio_to_maintain = new_ratio
        elif ratio_to_maintain != new_ratio:
            return False

    # All fee ratios are the same
    return True

# -----------------------------------------------------------------------------
# TESTING and MEMORY USEAGE
# -----------------------------------------------------------------------------
from HelperFunctions import get_memory_used


tests = [
    # {
    #     "intervals": [0, 10, 22],
    #     "fees": [1, 3, 1],
    #     "deliveries": [[8, 15],
    #                   [12, 21],
    #                   [15, 48],
    #                   [20, 17],
    #                   [23, 43]]
    # },
    {
        "intervals": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "fees": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "deliveries": [[0,32],
                       [1,58],
                       [2,10],
                       [3,23],
                       [4,59],
                       [5,4],
                       [6,36],
                       [7,52],
                       [8,38],
                       [9,7],
                       [10,43],
                       [11,54],
                       [12,7],
                       [13,15],
                       [14,12],
                       [15,29],
                       [16,48],
                       [17,1],
                       [18,47],
                       [19,21],
                       [20,13],
                       [21,51],
                       [22,7],
                       [23,20]]
    },
]

for t in tests:
    print("RESULT: ", solution(t["intervals"], t["fees"], t["deliveries"]))

get_memory_used()
