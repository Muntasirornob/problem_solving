class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter=0
        for index, i in enumerate(nums):
            if i != val:
                nums[counter]=i
                counter += 1
        return counter