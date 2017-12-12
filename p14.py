class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            for i in range(len(strs[0])):
                character = strs[0][i]
                for index, string in enumerate(strs):
                    if i == len(string) or string[i] != character:
                        return strs[0][:i]
            return strs[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(['a', 'b'])
    print(sol.longestCommonPrefix(['a'])
    print(sol.longestCommonPrefix(['aa', 'a'])
    print(sol.longestCommonPrefix(['aa', 'aa'])
