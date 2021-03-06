# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
# then the whole array will be sorted in ascending order, too.
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# 
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.



# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 
# 你找到的子数组应是最短的，请输出它的长度。
# 
# 示例 1:
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 
# 说明 :
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。



class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        compared_nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if compared_nums[i] != nums[i]:
                a.append(i)
        if a == []:
            return 0
        return max(a)-min(a)+1
