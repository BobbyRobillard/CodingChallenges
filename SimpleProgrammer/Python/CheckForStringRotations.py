######################################################################
# Check if a string (s1) is a rotation of another (s2).
######################################################################

# Rotate a string by one position
def rotate(string):
    return string[-1] + string[:-1]


def check_for_rotations(s1, s2):
    if len(s2) != len (s1): return False
    for i in range(len(s1)):
        s1 = rotate(s1)
        if s1 == s2: return True
    return False


######################################################################
# Examples and testing
######################################################################

s1 = "abcd"
s2 = "cdab"
result = check_for_rotations(s1, s2)
print("Is --> {0} a rotation of --> {1} ? {2}".format(s2, s1, str(result)))
assert result == True  # Simple unit test

# ---------------------------------------------------------------------
