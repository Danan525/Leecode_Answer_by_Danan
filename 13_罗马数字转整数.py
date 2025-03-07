class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = val.get(s[0])

        if len(s) < 2:
            return num

        i = 1
        while i < len(s):
            m = val.get(s[i])
            n = val.get(s[i-1])
            if m > n:
                num = num + m -2*n
            else:
                num = m + num
            i += 1
        return num


        