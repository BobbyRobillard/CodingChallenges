def solution(strings, patterns):

    if len(strings) != len(patterns):
        return False

    seen_strings = []
    seen_paterns = []

    for i in range(len(strings) - 1):
        seen_strings.append(strings[i])
        seen_paterns.append(patterns[i])
        if (strings[i] == strings[i + 1] and patterns[i] != patterns[i + 1]) or (
            strings[i] != strings[i + 1] and patterns[i] == patterns[i + 1]
        ):
            return False
        if strings[i] != strings[i + 1] and patterns[i] != patterns[i + 1]:
            if strings[i + 1] not in seen_strings:
                if patterns[i + 1] not in seen_paterns:
                    return False
    return True


strings = ["a", "b", "c"]
patterns = ["a", "b", "a"]
print("RESULT: {0}".format(str(solution(strings, patterns))))
