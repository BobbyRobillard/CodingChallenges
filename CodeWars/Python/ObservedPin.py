def get_pins(observed):
    others = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '9'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['9', '8', '9'],
        '0': ['0', '8'],
    }
    results = []
    for i in range(len(observed)):
        temp_result = [observed[:i] + other + observed[i+1:] for other in others[observed[i]]]
        results.append()
    return results

print("PINS: {}".format(get_pins('8')))
print("PINS: {}".format(get_pins('11')))
