class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for index in range(0, len(nums) - 2):
            
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            if nums[index] > 0:
                break

            target_add = 0 - nums[index]
            left_pointer = index + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                current_sum = nums[left_pointer] + nums[right_pointer]
                
                if target_add > current_sum:
                    left_pointer += 1
                elif target_add == current_sum:
                    result.append([nums[index], nums[left_pointer], nums[right_pointer]])
                    
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                        left_pointer += 1

                    left_pointer += 1
                    right_pointer -= 1
                else:
                    right_pointer -= 1
            
        return result