class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                map[str(n) + '_'] = i
            else:
                map[n] = i
        for n in nums:
            res = target - n
            if res == n:
                res = str(n) + '_'
            if res in map:
                return [map[n], map[res]]