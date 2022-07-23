class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Check edge cases
        d_len = len(digits)
        if d_len == 1 and digits[0] == 9:
            return [1,0]
        # Add one to array
        digits[d_len - 1] += 1
        # Carry result of addition
        for i in range(d_len - 1, 0, -1):
            if digits[i] >= 10:
                digits[i-1] += 1
                digits[i] -= 10
        # Check if overflowing max value, add new max to front if we are
        if digits[0] >= 10:
            digits[0] -= 10
            digits.insert(0, 1)
        return digits

s = Solution()
res = s.plusOne([9, 9, 9])
print(res)