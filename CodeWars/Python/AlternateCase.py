def alternate_case(s):
    return "".join([char.lower() if char.isupper() else char.upper() for char in s])

# Sample w/ 2 pairs found
input = ["Hello World", "cODEwARS"]
for item in input:
    print("\nInput: {0}\nAlternate Case: {1}".format(item, alternate_case(item)))

assert alternate_case("Hello World") == "hELLO wORLD" # Simple Unit Tests
assert alternate_case("cODEwARS") == "CodeWars" # Simple Unit Tests
