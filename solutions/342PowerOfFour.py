class Solution:
#     def isPowerOfFour(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 0 or num == 2 or math.sqrt(num) != int(math.sqrt(num)): return False
#         if num % 2 == 1 and num != 1: return False
        
#         flag = 1
#         while num != 0:
#             low = num & 1
#             if low == 1:
#                 flag -= 1
#                 if flag == -1:
#                     return False
#             num = num >> 1
        
#         return True
        
    def isPowerOfFour(self, num):
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 == num