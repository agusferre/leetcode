class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        matrix = []
        r = 0
        isZZ = False
        zzRow = numRows - 2 # 1 for array position
        res = ''
        for i, l in enumerate(s):
            if isZZ and numRows > 2:
                matrix[zzRow].append(l)
                zzRow -= 1
                if zzRow == 0:
                    zzRow = numRows - 2
                    isZZ = False
            else:
                if i < numRows:
                    matrix.append([])
                matrix[r].append(l)
                if r == numRows - 1:
                    r = -1
                    isZZ = True
                r += 1
        for row in matrix:
            res += ''.join(row)
        return res