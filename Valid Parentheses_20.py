class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start_brac = ['(','[','{']
        end_brac = [')',']','}']
        process_stack = list()
        
        for para in s:
            if para in start_brac:
                process_stack.append(para)
            elif para in end_brac:
                if len(process_stack)==0:
                    return False
                elif start_brac.index(process_stack[-1]) == end_brac.index(para) :
                    process_stack.pop()
                else: 
                    return False
            else:
                return False
        if len(process_stack) == 0:
            return True
        else:
            return False
        
# case: ']'
