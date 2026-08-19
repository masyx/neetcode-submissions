from collections import defaultdict

class Solution:
    # strs = ["act","pots","tops","cat","stop","hat"]
    # 
    # array of 26 that counts char freq
    # store array as a key in dict, value is the string
    # {
    #   "act" "cat"
    #   "pots","tops" "stop"
    #    "hat"
    # }
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            res[tuple(freq)].append(s)
        return list(res.values())