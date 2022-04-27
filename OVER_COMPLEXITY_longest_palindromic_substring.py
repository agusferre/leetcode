class Solution:
    def longestPalindrome(self, s: str) -> str:
        map = {}
        current = s[0]
        for i, l in enumerate(s):
            if l in map:
                print(l, 'letter')
                print(i, 'i')
                print(map[l], 'map')
                for app in map[l]:
                    print(app, 'app')
                    isPal = True
                    for j in range(1, i - app):
                        print(j, 'j')
                        if s[app + j] != s[i - j]:
                            isPal = False
                            break
                        print(isPal, 'isPal')
                    if isPal and i - app + 1 > len(current):
                        print('e')
                        current = s[app : i + 1]
                map[l].append(i)
            else:
                map[l] = [i]
        return current