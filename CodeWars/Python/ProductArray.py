from functools import reduce
from math import prod

# FIRST CORRECT SOLUTION #
def product_array(numbers):
    results = []
    for item in numbers:
        temp = numbers.copy()
        temp.remove(item)
        results.append(reduce(lambda x, y: x * y, temp))
    return results


# REFACTORED CORRECT SOLUTION #
def product_array(numbers):
    total_prod = prod(numbers)
    return [total_prod // item for item in numbers]


# EXAMPLE AND TESTING #
print(
    "\nInput: {0}\nProduct Array: {1}".format(
        "[3,27,4,2]", product_array([3, 27, 4, 2])
    )
)

assert product_array([3, 27, 4, 2]) == [216, 24, 162, 324]  # Simple Unit Tests
