class Solution(object)
    def removeDuplicates(self, nums)
        
        type nums List[int]
        rtype int
        
        m = len(nums)
        n = 1
        if m == 0 or m == 1
            return m
        else
            m = 1
            while m  len(nums)
                if nums[m] != nums [m-1]
                    nums[n] = nums[m]
                    m += 1
                    n += 1
                else
                    m += 1
            return n

