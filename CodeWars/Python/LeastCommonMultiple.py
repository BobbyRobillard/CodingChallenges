from functools import reduce
from numpy import lcm as lcm_internal # pip install numpy

def lcm(*args):
    return reduce(lcm_internal, args) if len(args) > 0 else 1

# EXAMPLE AND TESTING #
print("\nInput: {0}\nLeast Common Multiple: {1}".format("2, 5", lcm(2, 5)))

assert lcm(2, 5) == 10 # Simple Unit Tests
assert lcm() == 1 # Simple Unit Tests
assert lcm(9) == 9 # Simple Unit Tests
