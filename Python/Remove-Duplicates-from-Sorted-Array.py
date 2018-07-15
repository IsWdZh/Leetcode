# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].

# 从第一个元素开始比较，a不动，比较元素是否与nums[a]相等，若相等，则a不用动，i值一直往后推，若不相等，则将不相等的值赋予nums[a]后一位，a自加

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        a = 0
        n = len(nums)
        for i in range(n):
            if nums[a] != nums[i]:
                nums[a+1] = nums[i]
                a += 1
        return a+1
