class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split("/")
        stack = []

        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
            elif p == "." or p == "":
                continue
            else:
                stack.append(p)
            
        return "/" + "/".join(stack)