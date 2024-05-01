class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        row , col = (0,0)
        rev = numRows - 1
        matrix = [['' for _ in range(len(s))] for _ in range(numRows)]
        temp = "down"
        for c in s:
            matrix[row][col] = c
            if temp == "down":
                row+=1
            else:
                row-=1
                col+=1
            
            if row == numRows - 1:
                temp = "up"
            elif row == 0:
                temp = "down"
                
        result = ""
        for row in matrix:
            for char in row:
                if char != '':
                    result += char

        return result
