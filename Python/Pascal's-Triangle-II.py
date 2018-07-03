# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 3
# Output: [1,3,3,1]

# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?



# My Method: 纯粹偷懒，使用的之前写的杨辉三角生成的方法，然后提取出需要的那一行；

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1
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
        return a[rowIndex]
