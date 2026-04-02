class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        maping_list = {')':'(', '}':'{', ']':'['}
        stack = []
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c not in maping_list:
                stack.append(c)
            else:
                if stack:
                    last_element = stack.pop()

                    if last_element != maping_list[c]:
                        return False
                
                else:
                    return False
        
        return len(stack) == 0