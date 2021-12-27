from functools import reduce
from numpy import lcm as lcm_internal  # pip install numpy

# Problem assumes no negative input
# CORRECT SOLUTION 1 #
def lcm(*args):
    if 0 in args:
        return 0
    if len(args) == 0:
        return 1
    if len(args) == 1:
        return args[0]
    lcm_val = 1
    for arg in args:
        lcm_val = abs(lcm_val * arg) // math.gcd(lcm_val, arg)
    return lcm_val


# CORRECT SOLUTION 2 (REFACTORED) #
def lcm(*args):
    return reduce(lcm_internal, args) if len(args) > 0 else 1


# EXAMPLE AND TESTING #
print("\nInput: {0}\nLeast Common Multiple: {1}".format("2, 5", lcm(2, 5)))

assert lcm(2, 5) == 10  # Simple Unit Tests
assert lcm() == 1  # Simple Unit Tests
assert lcm(9) == 9  # Simple Unit Tests
