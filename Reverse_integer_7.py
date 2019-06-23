class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            tmp_num = int(str(x)[::-1])
            if tmp_num >= (2**31-1):
                return 0
            else:
                return tmp_num
        else:
            tmp_num = -(int(str(abs(x))[::-1]))
            if tmp_num <= -(2**31):
                return 0
            else:
                return tmp_num
