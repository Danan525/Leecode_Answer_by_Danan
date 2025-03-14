class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = 0

        while n < k:
            m = len(nums)-1
            i = nums[m]
            while m > 0:
                nums[m] = nums[m-1]
                m -= 1
            nums[0] = i
            n += 1
