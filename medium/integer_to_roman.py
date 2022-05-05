class Solution:
    def intToRoman(self, num: int) -> str:
        n = list(str(num))
        res = ''
        digitsDict = {1: {1: 'I', 5: 'V', 10: 'X'},2: {1: 'X', 5: 'L', 10: 'C'},3: {1: 'C', 5: 'D', 10: 'M'}}
        if len(n) == 4:
            for i in range(int(n[0])):
                res += 'M'
            n.pop(0)
        while len(n):
            d = int(n[0])
            if d == 0:
                n.pop(0)                
                continue
            romans = digitsDict[len(n)]
            if d == 4 or d == 9:
                res += romans[1] + romans[d+1]
                n.pop(0)
                continue
            if d >= 5:
                res += romans[5]
            while d % 5 != 0:
                res += romans[1]
                d -= 1
            n.pop(0)
        return res