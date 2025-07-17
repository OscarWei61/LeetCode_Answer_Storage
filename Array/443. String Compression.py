class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        
        write_index = 0
        read_index= 0

        while read_index < len(chars):
            char = chars[read_index]
            count_number = 0
            while read_index < len(chars) and chars[read_index] == char:
                count_number = count_number + 1
                read_index = read_index + 1
            
            chars[write_index] = char
            write_index = write_index + 1
           
            if count_number > 1:
                for c in str(count_number):
                    chars[write_index] = c
                    write_index = write_index + 1
            
            
        return write_index
            
            