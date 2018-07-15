# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

# My Method:
# 检查是否在list内，在的话返回索引；否则判断是否小于某个索引的数值大小，是的话则插入该数值前，索引即为该数值的索引；
# 再检查如果大于最后一个数值了，即该数值不存在，而且list内的数值均小于它，则其索引为最后一个
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return(nums.index(target))
        else:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
            if target > nums[-1]:
                return len(nums)
        
