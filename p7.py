class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = str(x)[1:][::-1]
            x = int(x) * (-1)
        if x >= 2**31 or x <= -(2**31):
            x = 0
        return x

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(-2147483648))