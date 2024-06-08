class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=(s.strip())
        z=x.split()
        y=z[-1]
        return len(y)
        
        