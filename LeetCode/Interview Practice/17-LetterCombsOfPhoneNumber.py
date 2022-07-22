class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        all_combinations = [''] if digits else []
        for digit in digits:
            current = list()
            for letter in digits_to_letters[digit]:
                for combination in all_combinations:
                    current.append(combination + letter)
            all_combinations = current
        return all_combinations

s = Solution()
print(s.letterCombinations("234"))