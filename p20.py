class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftBrackets = ['(', '[', '{']
        rightBrackets = [')', ']', '}']
        stackList = []
        
        for character in s:
            if character in leftBrackets:
                stackList.append(character)
            elif character in rightBrackets and len(stackList) != 0:
                 if character != stackList.pop():
                    return False
        if len(stackList) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution.isValid(']'))
    print(Solution.isValid('[()]'))
    print(Solution.isValid('[({)}]'))