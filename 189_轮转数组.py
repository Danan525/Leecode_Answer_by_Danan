class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = len(nums)

        if m < k:
            k = m-k%m
        else:
            k = m-k
        nums[:] = nums[k:m]+nums[:k]
