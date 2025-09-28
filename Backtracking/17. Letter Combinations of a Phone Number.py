class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        result = []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            
            letters = mapping[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        
        backtrack(0,  [])
        return result
