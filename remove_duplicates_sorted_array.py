# Example 1:
# Input: [1, 1, 2]
# Output: 2 (Unique elements: [1, 2])

# Example 2:
# Input: [0, 0, 1, 1, 1, 2, 2]
# Output: 3 (Unique elements: [0, 1, 2])

# Steps to Solve:
# Initialize count = 1 (to track unique elements).
# Iterate through the array starting from index 1:
# If the current element is not equal to the previous unique element:
# Replace nums[count] with nums[i].
# Increment count by 1.
# Return count (number of unique elements).
# Edge Cases: Handle arrays with size 0 or 1.


# basic operations :
# for i in range (1 ,len(nums))
# nums[count] = nums [i]


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0  # Return 0 if the array is empty

        count = 1  # Initialize count as 1 for the first element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]  # Update the array with the unique element
                count += 1  # Increment count for each unique element encountered

        return count
            