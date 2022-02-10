# -----------------------------------------------------------------------------
# CodeSignal Company Problem - Instacart - Busy Holidays
# https://app.codesignal.com/company-challenges/instacart/ZFhDcuS6BuDmhLBNN

# RUNTIME: 40-44ms
# MEMORY USED: 12.3MB
# -----------------------------------------------------------------------------
# ** TO-DO **
# 1) Fix can_take_order method, conditions aren't correct
# 2) Check during loop for ideal match
# -----------------------------------------------------------------------------
import operator


# Convert times of format "XX:YY" to seconds for easier comparison.
def conv_to_sec(time_to_conv):
    time_to_conv = time_to_conv.split(":")
    return int(time_to_conv[0])*60*60 + int(time_to_conv[1])*60


def can_tak_order(shopper, order, leadTime):
    # a) shopper start time >= order start time
    # b) order end time +
    return False


# Try to find the ideal shopper to take the order
def find_matching_shopper(shoppers, order, leadTime):
    best_shopper = None
    for s in shoppers:
        if can_tak_order(s, order, leadTime):
            if best_shopper == None: # Default to first if not set
                best_shopper = s
            else: # Compare current best with current shopper
                if conv_to_sec(best_shopper[1]) >= conv_to_sec(s[1]):
                    best_shopper = s
    return best_shopper


def solution(shoppers, orders, leadTimes):
    # Boundry checks
    if len(shoppers) < len(orders): return False
    if len(orders) == 0 or orders == None: return True
    # Try to make ideal matches between orders and shoppers
    while len(orders) > 0:
        if len(shoppers) == 0: return False # We've run out of shoppers
        for i, order in enumerate(orders):
            matched_shopper = find_matching_shopper(shoppers, order, leadTimes[i])
            print("Matched Shopper:", matched_shopper, "with order:", order)
            # Make sure a match was found
            if matched_shopper == None: return False
            # Remove matched items
            shoppers.remove(matched_shopper)
            del orders[i]
            del leadTimes[i]

    # Able to match all orders with a shopper
    return True

# -----------------------------------------------------------------------------
# TESTING and MEMORY USEAGE
# -----------------------------------------------------------------------------
from HelperFunctions import get_memory_used


tests = [
    {
        "shoppers": [["15:10", "16:00"],
                    ["17:40", "22:30"]],
        "orders":   [["17:30", "18:00"],
                    ["15:00", "15:45"]],
        "leadTime": [15, 30],
        "result": True
    },
    {
        "shoppers": [["15:10", "16:00"],
                    ["17:50", "22:30"],
                    ["13:00", "14:40"]],
        "orders":   [["14:30", "15:00"]],
        "leadTime": [15],
        "result": False
    },
    {
        "shoppers": [["23:00","23:59"],
                     ["22:30","23:30"]],
        "orders":   [["23:15","23:35"],
                     ["23:00","23:31"]],
        "leadTime": [20, 30],
        "result": True
    },
    {
        "shoppers": [["01:00","02:00"],
                     ["01:01","01:30"]],
        "orders":   [["01:00","02:00"],
                     ["01:11","02:00"]],
        "leadTime": [20, 20],
        "result": True
    },
]

for i, t in enumerate(tests):
    print("--------------------\nTEST #", i + 1)
    res = solution(t["shoppers"], t["orders"], t["leadTime"])
    try:
        assert res == t["result"]
        print("PASSED")
    except:
        print("FAILED, Expected:", t["result"], "| Got:", res)
        print("TESTING:", str(t))


get_memory_used()
