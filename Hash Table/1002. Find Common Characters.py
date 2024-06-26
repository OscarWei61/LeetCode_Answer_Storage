class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Better answer!
        # Initialize the list with the first word's characters frequencies
        common_count = [float('inf')] * 26
        
        # Iterate over each word to update the common_count
        for word in words:
            # Create a temporary count for the current word
            current_count = [0] * 26
            for char in word:
                current_count[ord(char) - ord('a')] += 1
            
            # Update the common_count to keep the minimum frequency
            for i in range(26):
                common_count[i] = min(common_count[i], current_count[i])
        
        # Create the result list based on common_count
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * common_count[i])
        
        return result
    
        # Worse Answer
        '''
        answer_list = []
        words_num = len(words) - 1
        for word_item in words[0]:
            target_char = word_item
            appear_count = 0
            for other_item in range(0, words_num + 1):
                if target_char in words[other_item]:
                    appear_count = appear_count + 1
            if appear_count == (words_num + 1):
                answer_list.append(target_char)
                for other_item in range(0, words_num + 1):
                    if target_char in words[other_item]:
                        words[other_item] = words[other_item].replace(target_char, '', 1)
        return answer_list
        '''
    
# Create an instance of the Solution class
solution = Solution()

# Call the commonChars function
result = solution.commonChars(["bella", "label", "roller"])

# Print the result
print(result)