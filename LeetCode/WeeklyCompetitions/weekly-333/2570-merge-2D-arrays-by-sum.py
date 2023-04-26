from collections import defaultdict


class Solution:
    def mergeArrays(self, nums1, nums2):
        max_val = 0
        # convert to dict
        dict1 = defaultdict(int)
        for el in nums1:
            max_val = max(max_val, el[0])
            dict1[el[0]] += el[1]
        dict2 = defaultdict(int)

        for el in nums2:
            max_val = max(max_val, el[0])
            dict2[el[0]] += el[1]

        # add result from each dict
        result = []
        for i in range(max_val + 1):
            temp = dict1[i] + dict2[i]
            if temp != 0:
                result.append([i, temp]) 
        return result


s = Solution()
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
res = s.mergeArrays(nums1, nums2)
print(res)