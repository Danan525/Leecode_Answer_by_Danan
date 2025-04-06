class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = len(height)
        pre_max = [0]*m
        post_max = [0]*m
        n = 0
        area = 0

        while n < len(height):
            if n == 0:
                pre_max[n] = height[n]
            else:
                pre_max[n] = max(pre_max[n-1],height[n])
            n += 1
        while m > 0:
            m -= 1
            if m == len(height)-1:
                post_max[m] = height[m]
            else:
                post_max[m] = max(post_max[m+1],height[m])
        while m < len(height):
            area = area+min(pre_max[m],post_max[m])-height[m]
            m += 1
        return area



