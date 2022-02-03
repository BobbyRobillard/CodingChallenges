######################################################################
# Reverse enumerables using recursion. Why? Because it's good practice!
######################################################################


def reverse_sentence(text):
    return " ".join(reverse_list(text.split(" ")))


# Reverse a list
def reverse_list(lst):
    if len(lst) == 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])


# Reverse a string
def reverse_string(lst):
    if len(lst) == 1:
        return lst
    return lst[-1] + reverse_string(lst[:-1])


######################################################################
# Examples and testing
######################################################################

to_reverse = "Testing"
reversed = reverse_string(to_reverse)
print("Reverse string, {0} --> {1}".format(to_reverse, reversed))
assert reversed == "gnitseT"  # Simple unit test

# ---------------------------------------------------------------------

to_reverse = [1, 2, 3, 4]
reversed = reverse_list(to_reverse)
print("Reverse list, {0} --> {1}".format(to_reverse, reversed))
assert reversed == [4, 3, 2, 1]  # Simple unit test

# ---------------------------------------------------------------------

to_reverse = "My code rocks!"
reversed = reverse_sentence(to_reverse)
print("Reverse sentence, {0} --> {1}".format(to_reverse, reversed))
assert reversed == "rocks! code My"  # Simple unit test
