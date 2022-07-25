class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {}
        count = 97
        for item in key:
            if item not in mp and item != " ":
                mp[item] = chr(count)
                count += 1
            if count == 123: # We have mapped all 26 letters
                break
        return "".join(mp[el] if el != " " else " " for el in message)

s = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
res = s.decodeMessage(key, message)
print(res)

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
res = s.decodeMessage(key, message)
print(res)