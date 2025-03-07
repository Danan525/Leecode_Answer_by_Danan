class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        m = 0
        n = 1

        while m < min(len(strs[n]) for n in range(len(strs))):
            n = 1
            while n < len(strs):
                if strs[0][m] == strs[n][m]:
                    n += 1
                else:
                  return strs[0][:m]  
            m += 1
        return strs[0][:m]


        