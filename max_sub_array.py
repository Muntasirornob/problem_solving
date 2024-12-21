# problem


# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# algo:

# Initialize current and sum to the first element of the array.
# Iterate through the array starting from the second element:
# Update current to be the maximum of current + value or value.
# Update sum to the maximum of current and sum.
# Return sum.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=nums[0]
        sum=nums[0]
        for value in nums[1:]:
                if current + value > value:
                    current = current + value  
                else:
                    current = value 
                
                # Update max_sum if current is larger
                if current > sum:
                    sum = current
            
        return sum
                    

