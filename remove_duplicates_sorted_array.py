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
            