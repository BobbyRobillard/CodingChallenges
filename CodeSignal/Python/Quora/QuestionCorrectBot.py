# -----------------------------------------------------------------------------
# CodeSignal Company Problem - Quora - Question Correct Bot
# https://app.codesignal.com/company-challenges/quora/sEStnM9dD9euiHWz6

# RUNTIME: ???
# MEMORY USED: ???
# -----------------------------------------------------------------------------
# ** TO-DO **
# 1) Solve the problem lol...
# -----------------------------------------------------------------------------


def solution(question):
    formatted = ""
    return formatted

# -----------------------------------------------------------------------------
# TESTING and MEMORY USEAGE
# -----------------------------------------------------------------------------
import psutil, os

tests = [
    {
        "question": " this isn't a relevant question , is it??? ",
        "result": "This isn't a relevant question, is it?"
    },
    {
        "question": "Is this answer correct?",
        "result": "Is this answer correct?"
    }
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
