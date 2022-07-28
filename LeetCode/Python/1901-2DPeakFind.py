class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        startCol = 0
        endCol = len(mat[0])-1
       
        while startCol <= endCol:
            maxRow = 0
            midCol = (endCol+startCol)//2
            
            for row in range(len(mat)):
                maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
            
            leftIsBig    =   midCol-1 >= startCol  and  mat[maxRow][midCol-1] > mat[maxRow][midCol]
            rightIsBig   =   midCol+1 <= endCol    and  mat[maxRow][midCol+1] > mat[maxRow][midCol]
            
            if (not leftIsBig) and (not rightIsBig):   # we have found the peak element
                return [maxRow, midCol]
            elif rightIsBig:             # if rightIsBig, then there is an element in 'right' that is bigger than all the elements in the 'midCol', 
                startCol = midCol+1     # so 'midCol' cannot have 'peakPlane'
            else:                           # leftIsBig
                endCol = midCol-1
                
        return []

s = Solution()
res = s.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]])
print(res)
