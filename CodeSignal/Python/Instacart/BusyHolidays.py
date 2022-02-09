# -----------------------------------------------------------------------------
# CodeSignal Company Problem - Instacart - Busy Holidays
# https://app.codesignal.com/company-challenges/instacart/ZFhDcuS6BuDmhLBNN

# RUNTIME: 40-44ms
# MEMORY USED: 12.3MB
# -----------------------------------------------------------------------------
import operator


# Convert times of format "XX:YY" to seconds for easier comparison.
def conv_to_sec(time_to_conv):
    time_to_conv = time_to_conv.split(":")
    return int(time_to_conv[0])*60*60 + int(time_to_conv[1])*60


def can_tak_order(shopper, order):
    # a) order start time <= shopper start time
    if conv_to_sec(order[0]) <= conv_to_sec(shopper[0]):
        # b) order start time + order fill time <= shopper end time
        if conv_to_sec(order[0]) + order[2] <= conv_to_sec(shopper[1]):
            # c) shopper start time + order fill time <= order end time
            if conv_to_sec(shopper[0]) + order[2] <= conv_to_sec(order[1]):
                return True
    return False


def solution(shoppers, orders, leadTime):
    # boundry checks
    if len(shoppers) < len(orders): return False
    if len(orders) == 0 or orders == None: return True
    # add leadTime to each order, simplifying function
    for i, t in enumerate(leadTime):
        orders[i].append(t)
    # sort shoppers by start time, secondly by end time
    shoppers.sort(key = operator.itemgetter(0, 1))
    # sort orders by start time, secondly by end time
    orders.sort(key = operator.itemgetter(0, 1))
    # try to make ideal matches between orders and shoppers
    while len(orders) > 0:
        for order in orders:
            order_complete = False
            for shopper in shoppers:
                if can_tak_order(shopper, order):
                    # remove the order, and the shopper who filled it
                    shoppers.remove(shopper)
                    orders.remove(order)
                    order_complete = True
                    break
            if not order_complete: return False # no shopper could take order
    # Able to match shoppers w/ orders
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
