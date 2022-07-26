"""
On day 1, one person discovers a secret.
You are given an integer delay, which means that each person will share the secret with a new person every day,
starting from delay days after discovering the secret. 

You are also given an integer forget, 
which means that each person will forget the secret forget days after discovering it. 

A person cannot share the secret on the same day they forgot it, or on any day afterwards.
Given an integer n, return the number of people who know the secret at the end of day n. 

Since the answer may be very large, return it modulo 109 + 7.
"""

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        days_heard = [1] # list of days each person heard the secret
        for i in range(2, n+1):
            for day in days_heard:
                # If they haven't forget the secret
                if i - day > forget:
                    days_heard.remove(day)
                # If they are past the delay time
                elif i - day >= delay:
                    # Tell the secret to someone new
                    days_heard.append(i)
        a = 1
        return len(days_heard) % (10**9 + 7)

s = Solution()
res = s.peopleAwareOfSecret(6,2,4)
print(res)
res = s.peopleAwareOfSecret(4,1,3)
print(res)