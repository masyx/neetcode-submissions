class Solution:
    # ["bat","bag","bank","band"]
    # get the first char from first str and verify that the rest of the strs have the same char, when a different char is found stop checking and return the common prefix that should be equal i - 1

    # edge case: ["a","a","a"]
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return s[:i]
        return strs[0]