class Solution:
    # ["bat","bag","bank","band"]
    # get the first char from first str and verify that the rest of the strs have the same char, when a different char is found stop checking and return the common prefix that should be equal i - 1

    # edge case: ["a","a","a"]
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        for i in range(len(strs[0])):
            idx = i
            curr_char = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != curr_char:
                    return s[:i]
        return strs[0][:idx + 1]