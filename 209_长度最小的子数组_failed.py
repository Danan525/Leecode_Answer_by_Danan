class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        ans = len(nums)

        if sum(nums[:len(nums)]) < target:
            return 0

        while left < len(nums):
            right = left+1
            while right <= len(nums):
                if sum(nums[left:right]) >= target:
                    ans = min((right-left),ans)
                    break
                else:
                    right += 1
            left += 1
        return ans