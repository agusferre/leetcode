class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        first = 0
        current = 0
        last = 0
        lastL = 0
        map = {}
        for i, l in enumerate(s):
            print(str(i) + 'idx')
            if l in map:
                array = map[l]
                print(array)
                if first == 0:
                    first = i
                print(current)
                print(last)
                lastL = array[len(array) - 1]
                current = i - max(last, lastL)
                print(current)
                if current > longest:
                    longest = current
                last = array[len(array) - 1]
                map[l].append(i)
            else:
                current += 1
                if current > longest:
                    longest = current
                map[l] = [i]
        print(longest)
        print(current)
        print(first)
        return max([longest, current, first]) if first != 0 else len(s)