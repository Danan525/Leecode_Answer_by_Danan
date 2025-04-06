class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        s = 0
        ans = len(nums)

        if sum(nums[:len(nums)]) < target:
            return 0

        while right < len(nums):
            s = s+nums[right]
            while s >= target:
                ans = min(ans,(right-left+1))
                s = s-nums[left]
                left += 1
            right += 1
        return ans