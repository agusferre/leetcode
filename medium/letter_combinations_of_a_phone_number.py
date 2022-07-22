from re import A
from attr import s


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        if len(digits) < 1:
            return []
        res = dict[digits[0]]
        i = 1
        while i < len(digits):
            partialRes = []
            for part in res:
                partialRes += self.combPart(part, dict[digits[i]])
            res = partialRes
            i += 1
        return res    

    def combPart(self, part, letters):
        res = []
        for l in letters:
            res.append(part + l)
        return res