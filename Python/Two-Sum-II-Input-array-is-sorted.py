# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
# 
# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# 
# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.



# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 
# 说明:
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 
# 示例:
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


# My Method:

# 解析: 方法很傻，从头遍历元素，用target减，得到的值如果存在于减去的那个数后面的数组中，则取下标（加上第一个数的下标值，再加一，因为不从0开始）
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers[0] <= target:
                temp = target - numbers[0]
                if temp in numbers[1:]:
                    index1 = 1
                    index2 = numbers[1:].index(temp)+2
                    return [index1, index2]
        for i in range(1, len(numbers)):
            if numbers[i] <= target and numbers[i] != numbers[i-1]:
                temp = target - numbers[i]
                if temp in numbers[i+1:]:
                    index1 = i+1
                    index2 = numbers[i+1:].index(temp)+i+2
        return [index1, index2]
