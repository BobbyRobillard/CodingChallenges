def arithmetic_arranger(input, solve=False):
    input = [item.split(" ") for item in input]
    return input

res = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
print(res)
