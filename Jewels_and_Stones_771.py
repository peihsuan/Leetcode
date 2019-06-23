class Solution(object):
    def numJewelsInStones(self, J, S):
        import re
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jew_list = list(J)
        return_list = list()
        for char in S:
            if char in jew_list:
                return_list.append(char)
        return len(return_list)
