class Solution:
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def search_rows(lo, hi, opt):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if opt == 'lower':
                    if '1' in image[mid] and (mid == 0 or '1' not in image[mid - 1]):
                        return mid
                    elif '1' in image[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if '1' in image[mid] and (mid == m - 1 or '1' not in image[mid + 1]):
                        return mid
                    elif '1' in image[mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                
        
        def search_cols(lo, hi, opt):
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if opt == 'lower':
                    if any(image[i][mid] == '1' for i in range(m)) and (mid == 0 or all(image[i][mid - 1] == '0' for i in range(m))):
                        return mid
                    elif any(image[i][mid] == '1' for i in range(m)):
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if any(image[i][mid] == '1' for i in range(m)) and (mid == n - 1 or all(image[i][mid + 1] == '0' for i in range(m))):
                        return mid
                    elif any(image[i][mid] == '1' for i in range(m)):
                        lo = mid + 1
                    else:
                        hi = mid - 1             
        
        
        m, n = len(image), len(image[0])
        
        top = search_rows(0, x, 'lower')
        bot = search_rows(x, m - 1, 'upper')
        
        left = search_cols(0, y, 'lower')
        right = search_cols(y, n - 1, 'upper')
                
        return (bot - top + 1) * (right - left + 1)