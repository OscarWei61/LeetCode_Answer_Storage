class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_count = Counter(magazine)

        for c in ransomNote:
            if mag_count[c] > 0:
                mag_count[c] = mag_count[c] - 1
            else:
                return False
        
        return True
