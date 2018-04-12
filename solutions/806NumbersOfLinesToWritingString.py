class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        max_width = 100
        lines, units = 1, 0
        
        for s in S:
            width = widths[ord(s)-ord('a')]
            if units + width > max_width:
                lines += 1
                units = width
            else:
                units += width
        
        return [lines, units]