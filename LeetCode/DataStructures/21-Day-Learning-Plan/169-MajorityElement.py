class Solution:
    # Initial solution, O(2n) --> O(n) time, O(n) space.
    def majorityElement(self, nums:list[int]) -> int:
        counts = {}
        for el in nums:
            if el in counts:
                counts[el] += 1
            else:
                counts[el] = 1
        return sorted(counts.items(), key=lambda x: x[1])[-1][0]

    # Single pass O(n) time, O(1) space.
    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
    def majorityElement(self, nums:list[int]) -> int:
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major

s = Solution()
res = s.majorityElement([3,2,3])
print(res)
res = s.majorityElement([2,2,1,1,1,2,2])
print(res)