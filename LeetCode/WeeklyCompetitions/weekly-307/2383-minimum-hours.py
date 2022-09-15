class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        energy_needed = sum(energy) - initialEnergy + 1
        energy_needed = energy_needed if energy_needed >= 0 else 0
        curr_exp = initialExperience
        exp_time = 0
        for exp in experience:
            if curr_exp <= exp:
               exp_time += exp - curr_exp + 1
            curr_exp += exp
        return energy_needed + exp_time

s = Solution()
# res = s.minNumberOfHours(5,3,[1,4,3,2],[2,6,3,1])
# print(res)
res = s.minNumberOfHours(1,1,[1,1,1,1],[1,1,1,50])
print(res)