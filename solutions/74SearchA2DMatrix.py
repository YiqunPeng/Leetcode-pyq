class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search_row(matrix, target, left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if matrix[mid][-1] >= target and matrix[mid-1][-1] < target:
                return mid
            elif matrix[mid][-1] < target:
                return search_row(matrix, target, mid+1, right)
            else:
                return search_row(matrix, target, left, mid-1)
                     
        
        def search_col(nums, target, left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return search_col(nums, target, left, mid-1)
            else:
                return search_col(nums, target, mid+1, right)
            
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        
        row = search_row(matrix, target, 0, len(matrix)-1)
        if row == -1:
            col = search_col(matrix[0], target, 0, len(matrix[0])-1)
        else:
            col = search_col(matrix[row], target, 0, len(matrix[0])-1)
        
        if col == -1:
            return False
        else:
            return True
        