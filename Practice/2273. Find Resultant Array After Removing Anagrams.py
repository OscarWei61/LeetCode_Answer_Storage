class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        stack = []
        stack.append(words[0])

        for word in words[1:]:
            if sorted(word) == sorted(stack[-1]):
                continue
            else:
                stack.append(word)
        
        return stack