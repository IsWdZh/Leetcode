# Given a binary array, find the maximum number of consecutive 1s in this array.
# 
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# 
# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000



# 给定一个二进制数组， 计算其中最大连续1的个数。
# 
# 示例 1:
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 
# 注意：
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。




class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count,count = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                count = 0
            max_count = max(count,max_count)
        return max_count
