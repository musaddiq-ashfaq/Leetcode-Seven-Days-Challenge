class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            row,col=i,0
            diagonal = []
            while row<m and col<n:
                diagonal.append(mat[row][col])
                row+=1
                col+=1
                diagonal.sort()
            while diagonal:
                mat[row-1][col-1]=diagonal.pop()
                row-=1
                col-=1

        for i in range(n):
            row,col = 0,i
            diagonal = []
            while row<m and col<n:
                diagonal.append(mat[row][col])
                row+=1
                col+=1
                diagonal.sort()
            while diagonal:
                mat[row-1][col-1]=diagonal.pop()
                row-=1
                col-=1
        return mat