class Solution:
    # use an array as a map
    # O(n) time, where n is the length of s or t
    # O(1) space, since we use an array of length 26
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        for count in counts:
            if count != 0:
                return  False
        return True 
        
        