class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i, l in enumerate(strs[0]):
            for s in strs:
                if len(s) == i or s[i] != l:
                    return res
            res += l
        return res