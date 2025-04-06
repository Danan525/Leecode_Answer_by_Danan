class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        m = 0
        max_step = 0

        if nums[0] == 0:
            if len(nums) == 1:
                return True
            return False

        while m < len(nums):
            if max_step >= (len(nums)-1):
                return True
            if m <= max_step:
                max_step = max(max_step,(m+nums[m]))
            m += 1
        return False


        