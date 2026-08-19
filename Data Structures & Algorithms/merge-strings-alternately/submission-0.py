class Solution:
    # word1 = "", word2 = "xyz"
    # smallest = 3
    # res = "axbycz"
    # i = 3
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        smallest = min(n, m)

        i = 0
        res = ""
        while i < smallest:
            res += f"{word1[i]}{word2[i]}"
            i += 1
        
        if n != m:
            if i >= len(word1):
                res += word2[i:]
            else:
                res += word1[i:]

        return res

        
        