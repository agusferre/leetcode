class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = list(str(x))
        original = ''.join(n)
        n.reverse()
        reverse = ''.join(n)
        return original == reverse