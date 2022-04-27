class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i, l in enumerate(s):
            nextL = s[i+1] if i+1 < len(s) else 'null'
            if l == 'I':
                if nextL == 'V' or nextL == 'X':
                    sum -= 1
                else:
                    sum += 1
            elif l == 'V':
                sum += 5
            elif l == 'X':
                if nextL == 'L' or nextL == 'C':
                    sum -= 10
                else:
                    sum += 10
            elif l == 'L':
                sum += 50
            elif l == 'C':
                if nextL == 'D' or nextL == 'M':
                    sum -= 100
                else:
                    sum += 100
            elif l == 'D':
                sum += 500
            elif l == 'M':
                sum += 1000
        return sum