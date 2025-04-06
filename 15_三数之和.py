class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # i < j < k
        i = 0
        ans = []


        while i < (len(nums)-2):
            j = i+1
            k = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while j < k:
                if nums[i]+nums[j]+nums[k] > 0:
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            i += 1
        return ans

