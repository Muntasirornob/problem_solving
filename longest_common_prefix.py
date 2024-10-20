class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Loop over the rest of the array
        for s in strs[1:]:
            # Check if the current string starts with the prefix
            while not s.startswith(prefix):
                # Shorten the prefix from the end by 1 character
                prefix = prefix[:-1]

                # If the prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""

        return prefix