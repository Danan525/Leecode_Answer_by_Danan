class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)-1

        if m == 0:
            return 1

        n = 0

        if s[m] == ' ':
            while m in range(len(s)):
                m -= 1
                if s[m] != ' ':
                    break

        while m in range(len(s)):
            n += 1
            m -= 1
            if s[m] == ' ':
                return n
        return n