def solution(prices, notes, x):
    # 1) convert notes to array of %'s
    percents = []
    for note in notes:
        note = note.split(" ")
        if "higher" in note:
            percents.append(-1 * float(note[0].replace("%", "")))
        elif "lower" in note:
            percents.append(float(note[0].replace("%", "")))
        else:
            percents.append(0)

    # 2) apply percentage change to each item in prices, record difference in price
    changes = []
    for i, price in enumerate(prices):
        changes.append(price - (price / (1 - percents[i]/100)))

    # 3) check if the sum of the differences if within tolerance
    return x >= round(sum(changes), 4)


prices = [110, 95, 70]
notes = [
    "10.0% higher than in-store",
     "5.0% lower than in-store",
     "Same as in-store"
 ]
x = 5
print("RESULT: {0}".format(str(solution(prices, notes, x))))
prices = [40, 40, 40, 40]
notes = [
    "0.001% higher than in-store",
 "0.0% lower than in-store",
 "0.0% higher than in-store",
 "0.0% lower than in-store"
 ]
x = 0
print("RESULT: {0}".format(str(solution(prices, notes, x))))
