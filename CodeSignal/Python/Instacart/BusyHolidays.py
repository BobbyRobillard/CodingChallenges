# -----------------------------------------------------------------------------
# CodeSignal Company Problem - Instacart - Busy Holidays
# https://app.codesignal.com/company-challenges/instacart/ZFhDcuS6BuDmhLBNN

# RUNTIME: 40-44ms
# MEMORY USED: 12.3MB
# -----------------------------------------------------------------------------

def solution(shoppers, orders, leadTime):
    return True

# -----------------------------------------------------------------------------
# TESTING and MEMORY USEAGE
# -----------------------------------------------------------------------------
from HelperFunctions import get_memory_used


tests = [
    {
        "shoppers": [["15:10", "16:00"],
                    ["17:40", "22:30"]],
        "orders": [["17:30", "18:00"],
                  ["15:00", "15:45"]],
        "leadTime": [15, 30]
    },
]

for t in tests:
    print("RESULT: ", solution(t["shoppers"], t["orders"], t["leadTime"]))

get_memory_used()
