# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order
# of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12], after
# calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# 遍历数组，将检测到的不为0的数依次移动到前面，记录移动次数，然后根据移动次数，将数组后几位改为0即可

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        n = len(nums)
        for i in range(n):
             if not nums[i] == 0:
                nums[pos] = nums[i]
                pos += 1
        for j in range(n-pos,0,-1):
            nums[-j] = 0
