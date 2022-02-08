def solution(s, markers):
    result = ""
    i = 0
    ignoring = False
    while i < len(s) - 1:
        if s[i] in markers:
            ignoring = True
            i += 1
        elif "\n" in str(s[i : i + 2]):
            ignoring = False
            result += "\n"
            i += 2
        elif not ignoring:
            result += s[i]
            i += 1
        else:
            i += 1
    return result.strip()


print(
    "STRIP COMMENTS: {}".format(
        solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    )
)
