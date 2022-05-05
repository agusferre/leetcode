class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        shortPos, shortLen = 0, height[0] if height[0] >= height[n-1] else n-1, height[n-1]
        lowPivPos, lowPiv
        for i, h in enumerate(height):
            if h > shortLen and 


    def area(self, t1, t2):
        return (t2[0] - t1[0]) * min(t1[1], t2[1])



    1 1 2 1 1 2