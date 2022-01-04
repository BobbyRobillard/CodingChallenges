def canal_mania(low_queue, high_queue, lock_length):
    low_sum = sum(2 * boat + 2 for boat in low_queue) + 2 if len(low_queue) > 0 else 0
    high_sum = sum(2 * boat + 2 for boat in high_queue) + 2 if len(high_queue) > 0 else 0
    return low_sum + high_sum

print("\n---Canal Mania---\n{0}".format(canal_mania([], [4, 4, 7, 2, 8, 5], 8)))
