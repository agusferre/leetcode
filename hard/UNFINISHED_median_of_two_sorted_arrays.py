class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        med1 = nums1[n/2]
        med2 = nums2[m/2]
        