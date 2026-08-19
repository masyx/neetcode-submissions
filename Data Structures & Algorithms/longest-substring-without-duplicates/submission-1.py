class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        for l in range(len(s) - 1):
            seen = {s[l]}
            r = l + 1
            curr_res = 1
            while r < len(s):
                if s[r] not in seen:
                    seen.add(s[r])
                    curr_res += 1
                    res = max(res, curr_res)
                    r += 1
                else:
                    break
        return res
        