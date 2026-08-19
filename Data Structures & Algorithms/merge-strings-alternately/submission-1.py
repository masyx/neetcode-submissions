class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        smallest = min(n, m)

        res = []
        for i in range(smallest):
            res.extend([word1[i], word2[i]])

        if n < m: # word1 shorter than word2
            res.extend(word2[smallest:])
        else:
            res.extend(word1[smallest:])

        return "".join(res)