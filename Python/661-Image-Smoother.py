# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell 
# becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# 
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].





# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，
# 如果周围的单元格不足八个，则尽可能多的利用它们。
# 
# 示例 1:
# 
# 输入:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# 输出:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# 
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 
# 注意:
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。



# 解析：定义了一个数组move_marix，通过索引下标+1、-1来得到以i，j为中心的9个数的索引值，然后通过judge方法判断是否出界，如果出界了，则不进行累加操作
#       也不增加count值（用来统计有多少数参与累加了）。最后，由于要向下取整，所以直接将得到的数值int一下即可。

# 另：在此之前，应新建一个同类型的数组，用来存放计算后的数值，由于数组内还包含数组，所以应使用copy.deepcopy()方法，而不能简单的使用newM = M
#     或newM = copy(M),因为如果这样的话，一旦修改了newM数组，则M数组也会相应的发生变化；



class Solution:
    def judge(self, x,y,i,j):
        return (True if i<x and j<y and i>=0 and j>=0 else False)
    def imageSmoother(self,M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        x = len(M)
        y = len(M[0])
        newM = copy.deepcopy(M)
        move_matrix = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]   # 根据索引加1减1 找到9个位置的索引值，先横向再纵向
        for i in range(x):
            for j in range(y):
                localsum, count = 0, 0
                for k in range(len(move_matrix)):         # 每个M[i][j]对应查找9个周边位置，判断是否在范围内
                    temi = i + move_matrix[k][0]
                    temj = j + move_matrix[k][1]
                    if self.judge(x, y ,temi,temj):
                        localsum += M[temi][temj]
                        count += 1
                newM[i][j] = int(localsum/count)
        return newM
        





