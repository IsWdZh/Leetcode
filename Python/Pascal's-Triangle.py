# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# My Method:  首先使用列表生成式生成一个同样形式的二维数组；
#             然后根据 a[i][j] = a[i-1][j-1] + a[i-1][j]     /  a[i][0] = 0（首） / a[i][j] = 0（尾）i = j



class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """                                          # a[i,j] = a[i-1,j-1] + a[i-1,j]
        a = [[0 for j in range(i+1)] for i in range(numRows)]
        if numRows == 0:
            return a
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    a[i][0] = 1
                    a[i][j] = 1
                else:
                    a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
        return a
