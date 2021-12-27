def even_last(numbers):
    return 0 if len(numbers) == 0 else sum(numbers[x] for x in range(0, len(numbers), 2)) * numbers[len(numbers)-1]


# EXAMPLE AND TESTING #
print(
    "\nInput: {0}\nEven Times Last: {1}".format(
        "[2,3,4,5]", even_last([2,3,4,5])
    )
)

assert even_last([2,3,4,5]) == 30  # Simple Unit Tests
