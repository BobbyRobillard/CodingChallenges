class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        waiting = {}
        day = 0
        index = 0
        while index < len(tasks):
            day += 1
            task = tasks[index]
            for key in waiting:
                waiting[key] -= 1
            if task not in waiting:
                waiting[task] = space
                index += 1
            else:
                if waiting[task] <= 0:
                    del waiting[task]
        return day - 1

s = Solution()
res = s.taskSchedulerII([1,2,1,2,3,1], 3)
print(res)
res = s.taskSchedulerII([5,8,8,5], 2)
print(res)
