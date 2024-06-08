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