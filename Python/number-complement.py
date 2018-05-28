# Time:  O(1)
# Space: O(1)

# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.
#
# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

# My Method:
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = len(bin(num))-2
        b = 2**a-1
        return b-num
# Explanation: Use bin() to convert num to binary / Binary has two prefixes--0b,So you should subtract 2;
               2**Binary length is The same length binary maximum + 1 / So subtract 1 is the same length binary maximum
               subtract num is it's complement
# Such as: 5      binary is: ob101       a = 3
           2**3 is   111 + 1 = 1000, So subtract 1 is 111
           111 - 101 is it's completement;
           
# Another kind of expression：
      return 2 ** (len(bin(num)) - 2) - 1 - num
      
      
      
# Another method：
class Solution2(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num
               
