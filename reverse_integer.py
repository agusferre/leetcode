class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        isNeg = x < 0
        n = list(str(abs(x)))
        while n[len(n) - 1] == '0': # clean 0s
            n.pop()
        if isNeg:
            n.append('-')
        n.reverse()
        n = int(''.join(n))
        return 0 if abs(n) > 2**31 or n == 2**31 - 1 else n