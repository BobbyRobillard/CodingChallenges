class Solution:
    def __init__(self):
        self.closing = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for el in s:
            if el in self.closing:
                stack.insert(0, el)
            elif not stack:
                return False
            else:
                if el != self.closing[stack[0]]:
                    return False
                else:
                    del stack[0]
        return not stack


s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("[]({})"))
print(s.isValid("{}}"))
print(s.isValid("({}[[([{}])]])"))
