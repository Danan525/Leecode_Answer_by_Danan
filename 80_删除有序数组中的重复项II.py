class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        n = 0

        while m < len(nums):
            if m < 2 or nums[m] != nums[n-2]:
                nums[n] = nums[m]
                n += 1
            m += 1
        return n

        