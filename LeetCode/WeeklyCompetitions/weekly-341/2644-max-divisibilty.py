class Solution:
    def maxDivScore(self, nums, divisors):
        results = []
        # For each divisor
            # For each number
                # Count num of equal divisions
        for d in divisors:
            results.append(sum(1 if num % d == 0 else 0 for num in nums))
        return divisors[results.index(max(results))]

s = Solution()
print(s.maxDivScore([4,7,9,3,9], [5,2,3]))