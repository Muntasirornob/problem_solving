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
                    
