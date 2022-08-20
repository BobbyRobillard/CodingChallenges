class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        to_letter = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "h",
            8: "i",
            9: "j",
            10: "k",
            11: "l",
            12: "m",
            13: "n",
            14: "o",
            15: "p",
            16: "q",
            17: "r",
            18: "s",
            19: "t",
            20: "u",
            21: "v",
            22: "w",
            23: "x",
            24: "y",
            25: "z",
        }
        to_number = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25,
        }
        for shift in shifts:
            t = ""
            if shift[2]: # Shift each item forward
                for i in range(shift[0], shift[1]+1):
                    curr_num_val = to_number[s[i]]
                    if curr_num_val + 1 > 25:
                        t += to_letter[0]
                    else:
                        t += to_letter[curr_num_val + 1]
            else: # Shift each item backward
                for i in range(shift[0], shift[1]+1):
                    curr_num_val = to_number[s[i]]
                    if curr_num_val - 1 < 0:
                        t += to_letter[25]
                    else:
                        t += to_letter[curr_num_val - 1]
            s = s[:shift[0]] + t + s[shift[1]+1:]
        return s

s = Solution()
print(s.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]))
print(s.shiftingLetters("dztz", [[0,0,0],[1,1,1]]))
print(s.shiftingLetters("xuwdbdqik", [[4,8,0],[4,4,0],[2,4,0],[2,4,0],[6,7,1],[2,2,1],[0,2,1],[8,8,0],[1,3,1]]))
