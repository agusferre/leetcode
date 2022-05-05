class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #OUT FOR TIME COMPLEXITY IN LAST TEST
        res = []
        dict = {}
        if len(nums) < 3:
            return res
        for n in nums:
            if n not in dict:
                dict[n] = False
            else:
                dict[n] = True
        for i, n in enumerate(nums[:len(nums)-1]):
            for n2 in nums[i+1:]:
                if -n-n2 in dict:
                    if (n != n2 and n != -n-n2 and n2 != -n-n2) or dict[-n-n2]:
                        arr = sorted([n, n2, -n-n2])
                        if arr not in res:
                            res.append(arr)
        if nums.count(0) > 2 and [0, 0, 0] not in res:
            res.append([0, 0, 0])
        elif nums.count(0) < 3 and [0, 0, 0] in res:
            res.remove([0, 0, 0])
        return res
        
        
        
        
        """
        res = []
        defRes = []
        if len(nums) < 3:
            return res
        for ii, i in enumerate(nums[:len(nums)-2]):
            for ij, j in enumerate(nums[ii+1:len(nums)-1]):
                for k in nums[ii+ij+2:]:
                    if i + j + k == 0:
                        res.append(sorted([i, j, k]))
        print(res)
        for i in res:
            if i not in defRes:
                defRes.append(i)
        return defRes"""