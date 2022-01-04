import math

# def thirt_calculation(n):
#     # Reverse number
#     reversed = str(n)[::-1]
#     # Find repeating sequence (seq.)
#     curr_power = 0
#     results_sum = 0
#     repeating_sequence = []
#     while True:
#         next_result = (int(math.pow(10, curr_power)) % 13)
#         if next_result in repeating_sequence and (len(repeating_sequence) >= len(reversed)):
#             repeating_sequence.append(next_result)
#             # Multiply each item in seq. by same position in reversed number
#             results_sum = sum([repeating_sequence[i] * int(reversed[i]) for i in range(0, len(reversed))])
#             break
#         repeating_sequence.append(next_result)
#         curr_power += 1
#     return results_sum

def thirt_calculation(n):
    # Reverse number
    reversed = str(n)[::-1]
    # Find repeating sequence (seq.)
    return sum((int(math.pow(10, curr_power)) % 13) * int(reversed[curr_power]) for curr_power in range(0, len(reversed)))

def thirt(n):
    numbers_found = []
    # Repeat process until number is stationary.
    while True:
        next_result = thirt_calculation(n)
        if next_result in numbers_found:
            return next_result
        numbers_found.append(next_result)
        n = next_result

print("\n---Thirt---\n{0}".format(thirt(85299258)))
