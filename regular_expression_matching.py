class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == len(p) == 0:
            return True
        if len(s) == 0 and len(p) > 1 and p[1] == '*':
            return self.isMatch('', p[2:])
        if len(p) == 0 or len(s) == 0:
            return False
        if len(s) == len(p) == 1:
            return s[0] == p[0] or p == '.'
        if len(p) > 1 and ((p[-1] != '*' and p[-1] != '.' and p[-1] != s[-1]) or (p[1] != '*' and p[0] != '.' and s[0] != p[0])): #Complexity tweak
            return False
        if len(s) == 1 and p[1] == '*':
            if p.count('*') < int(len(p)/2):
                return False
            i = 1
            ok = False
            broken = False
            while i < len(p):
                if p[i-1] == '.' or p[i-1] == s and not ok:
                    ok = True
                i += 2
                if i < len(p) and p[i] != '*':
                    if not broken and (p[i-1] == '.' or p[i-1] == s):
                            ok = True
                            i += 1
                            broken = True
                    else:
                        return False
            return (ok and len(p) == i-1) or self.isMatch(s, p[2:])
        if p[0:2] == '.*':
            if len(p) == 2:
                return True
            for i, l in enumerate(s):
                if (l == p[2] or p[2] == '.' or (len(p) > 3 and p[3] == '*')) and self.isMatch(s[i:], p[2:]):
                    return True
            return self.isMatch(s[1:], p)
        if len(p) > 1 and p[1] == '*':
            if len(p) == 2:
                for i, l in enumerate(s):
                    if l != p[0] and len(s) != 0:
                        return False
                return True
            if s[0] != p[0]:
                return self.isMatch(s, p[2:])
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                i += 1
                if self.isMatch(s[i:], p[2:]) or len(s) == 1:
                    return True
            return self.isMatch(s, p[2:])
        if s[0] == p[0] or p[0] == '.':
            return self.isMatch(s[1:], p[1:])
        return False
