# -----------------------------------------------------------------------------
# CodeSignal Company Problem - Quora - Question Correct Bot
# https://app.codesignal.com/company-challenges/quora/sEStnM9dD9euiHWz6

# RUNTIME: 84ms
# MEMORY USED: 12.19MB
# -----------------------------------------------------------------------------
# ** TO-DO **
# 1) Solve the problem lol...
# -----------------------------------------------------------------------------
import re


def solution(question):
    # Regex replace all occurences of two or more spaces with one space
    formatted = re.sub("\s+", " ", question)
    # Strip any leading and trailing whitespace
    formatted = formatted.strip()
    # Remove ?s, add single ? at end (don't know if ? are allowed in the rest of the string)
    formatted = formatted.replace("?", "")
    formatted += "?"
    # Capitalize the first letter in the string
    formatted = formatted[0].upper() + formatted[1:]
    # Regex replace all spacing around commas to match format
    formatted = re.sub(",", ", ", formatted)
    formatted = re.sub("\s+,\s*", ", ", formatted)
    return formatted

# -----------------------------------------------------------------------------
# TESTING and MEMORY USEAGE
# -----------------------------------------------------------------------------
import psutil, os

tests = [
    {
        "question": "    this isn't a relevant question , is it??? ",
        "result": "This isn't a relevant question, is it?"
    },
    {
        "question": "Is this answer correct?",
        "result": "Is this answer correct?"
    },
    {
        "question": "  Is,it    correct    ,    question",
        "result": "Is, it correct, question?"
    },
    {
        "question": "questionword ,anotherquestionword,",
        "result": "Questionword, anotherquestionword, ?"
    },
    {
        "question": "where is F.A.Q.?",
        "result": "Where is F.A.Q.?"
    },
    {
        "question": "a,b,c,d,e ",
        "result": "A, b, c, d, e?"
    },
]

for i,t in enumerate(tests):
    print("--------------------\nTEST #", i + 1, end=" | ")
    res = solution(t["question"])
    try:
        assert res == t["result"]
        print("PASSED")
    except:
        print("FAILED\nExpected:", t["result"], "\nGot:", res)
        print("TESTING:", str(t["question"]))

process = psutil.Process(os.getpid())
print("--------------------\nMAX MEMORY: " + str(process.memory_info().rss / 1000000) + "MB")  # in mb
