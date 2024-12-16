# LeetCode 1: Two Sum

# Example
# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1] (Indices of the numbers that add up to the target)


# Steps to Solve:
# 1. **Initialize** an empty dictionary `num_dict`.  
# 2. **Iterate** through each number in the array.  
#    - Calculate the complement: `complement = target - num`.  
#    - **Check** if the complement exists in `num_dict`.  
#      - If yes: Return the indices of the complement and current number.  
#      - Else: Add the number and its index to `num_dict`.  


# **Basic Dictionary Operations (Python):**  
# - Initialize: `demo_dict = {1: 3, 2: 2}`  
# - Add key-value pair: `demo_dict[4] = 3`  
# - Access values: `print(demo_dict[4])`  
# - Output: `{1: 3, 2: 2, 4: 3}`  


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # Create an empty dictionary to store elements and their indices

        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed for the current number

            if complement in num_dict:
            # If the complement exists in the dictionary, return its index and the current index
                return [num_dict[complement], index]
            else:
            # Add the current number and its index to the dictionary
                num_dict[num] = index

    # If no solution is found
        return []