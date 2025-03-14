class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = 0

        while n < len(haystack):
            i = 0
            while i < len(needle) and (n+i) < len(haystack):
                if haystack[n+i] != needle[i]:
                    break
                else:
                    i += 1
                    if i == len(needle):
                        return n
            n += 1
        return -1


