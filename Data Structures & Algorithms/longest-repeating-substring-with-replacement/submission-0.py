
class Solution:
    #       r
    #   l
    #  0123456
    # "AAABABB"
    # A = 3, B = 2
    # max_freq = 4
    # res = 5
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = [0] * 26
        l = 0
        max_freq = 0
        for r, char in enumerate(s):
            counts[ord(char) - ord('A')] += 1
            max_freq = max(max_freq, counts[ord(char) - ord('A')])
            if (r - l + 1) - max_freq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

        