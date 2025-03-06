class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m = 0
        k = 0

        while m < len(nums):
            if nums[m] != val:
                nums[k] = nums[m]
                k += 1
            m += 1
        return k


        