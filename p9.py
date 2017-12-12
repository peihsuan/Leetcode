# 回文
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            result = False
        else:
            x = str(x)
            intLen = len(x)
            pivotIndex = intLen // 2
            if x[0:pivotIndex + 1] == x[:: -1][0:pivotIndex + 1]:   # 往前數前幾位，倒過來前幾位都相等，即回文
                result = True
            else:
                result = False
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(12321))
    print(sol.isPalindrome(-123))
    print(sol.isPalindrome(5432))
    print(sol.isPalindrome(11))
