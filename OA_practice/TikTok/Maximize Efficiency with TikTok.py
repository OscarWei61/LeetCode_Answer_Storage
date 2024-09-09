class Solution:
    def maximizeEfficiencyProduct(self, efficiencyScores):
        
        if len(efficiencyScores) == 5:
            total = 1
            for num in efficiencyScores:
                total = total * num
            return total

        efficiencyScores.sort()
        total_1 = 1
        for index in range(len(efficiencyScores) - 1, len(efficiencyScores) - 6, -1):
            total_1 = total_1 * efficiencyScores[index]

        total_2 = efficiencyScores[-1] * efficiencyScores[-2] * efficiencyScores[-3] * efficiencyScores[0] * efficiencyScores[1]
        total_3 = efficiencyScores[-1] * efficiencyScores[2] * efficiencyScores[3] * efficiencyScores[0] * efficiencyScores[1]
        return max(total_1, total_2, total_3)

# Example usage
efficiencyScores = [6, 1, 2, 8, 1]
s = Solution()
print(s.maximizeEfficiencyProduct(efficiencyScores))  # Output: 96

# Example usage
efficiencyScores = [-10, -3, 1, 2, 4, 5, 6]
s = Solution()
print(s.maximizeEfficiencyProduct(efficiencyScores))  # Output: 3600