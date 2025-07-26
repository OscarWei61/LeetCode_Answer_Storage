from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        count1 = {}
        count2 = {}

        for w in word1:
            if w in count1:
                count1[w] = count1[w] + 1
            else:
                count1[w] = 1
        
        for w in word2:
            if w in count2:
                count2[w] = count2[w] + 1
            else:
                count2[w] = 1

        key1 = []
        for k in count1:
            key1.append(k)
        
        key1.sort()


        key2 = []
        for k in count2:
            key2.append(k)
        
        key2.sort()

        if key1 != key2:
            return False
        
        freq1 = []
        for k in count1:
            freq1.append(count1[k])
        freq1.sort()


        freq2 = []
        for k in count2:
            freq2.append(count2[k])
        freq2.sort()

        if freq2 != freq1:
            return False

        return True