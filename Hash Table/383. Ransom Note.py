class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        wordsdict = {}
        for ransom_char in ransomNote:
            index = ord(ransom_char) - ord('a')
            if (index) in wordsdict:
                wordsdict[index] += 1
            else:
                wordsdict[index] = 1

        for magazine_char in magazine:
            index = ord(magazine_char) - ord('a')
            if (index) in wordsdict:
                wordsdict[index] -= 1
                if wordsdict[index] == 0:
                    del wordsdict[index]
        if len(wordsdict) == 0:
            return True
        else:
            return False