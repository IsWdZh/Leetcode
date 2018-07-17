# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the number 0 itself.
 
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.



# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。

# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


# 逆向遍历整个数组，如果不为9，则加一输出即可；如果为9，则置该位为0，继续找前面的，直到找到不为9的，然后将该位加一，再输出；
# 如果遍历结束了都没返回，说明数组内的数全为0，则只需将第一个数置1，后面再加个0即可；


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
        
