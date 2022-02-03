######################################################################
# Check if a string (s1) is a rotation of another (s2).
######################################################################

# Rotate a string by one position
def rotate(string, n=1):
    return string[-n:] + string[:-n]


def check_for_rotations(s1, s2):
    if len(s2) != len (s1): return False
    return any(rotate(s1, i) == s2 for i in range(1, len(s2)))



######################################################################
# Examples and testing
######################################################################

s1 = "abcd"
s2 = "bcda"
result = check_for_rotations(s1, s2)
print("Is --> {0} a rotation of --> {1} ? {2}".format(s2, s1, str(result)))
# assert result == True  # Simple unit test

# ---------------------------------------------------------------------
