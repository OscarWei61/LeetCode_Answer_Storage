class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        version1_element = version1.split('.')
        version2_element = version2.split('.')

        for index in range(0, max(len(version1_element), len(version2_element))):
            if index + 1 > len(version1_element):
                version1_e = 0
            else:
                version1_e = int(version1_element[index])
            if index + 1 > len(version2_element):
                version2_e = 0
            else:
                version2_e = int(version2_element[index])

            if version1_e > version2_e:
                return 1
            elif version2_e > version1_e:
                return -1
        
        return 0
                