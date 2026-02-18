class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix = prefix + char

            index = bisect.bisect_left(products, prefix)

            suggestions = []

            for j_index in range(index, min(index + 3, len(products))):
                if products[j_index].startswith(prefix):
                    suggestions.append(products[j_index])
                else:
                    break
            
            result.append(suggestions)
        
        return result   