class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            m = (l+r)//2



            if (matrix[m][0] == target or matrix[m][len(matrix[m])-1] == target): return True
            if (matrix[m][0] < target and matrix[m][len(matrix[m])-1] > target):
                innerL, innerR = 0, len(matrix[m])-1
                
                while innerL < innerR:
                    innerM = (innerL + innerR)//2

                    if matrix[m][innerM] == target: return True

                    if matrix[m][innerM] > target: innerR = innerM-1
                    else: innerL = innerM+1

                return False

            if matrix[m][0] > target: r = m-1
            else: l = m+1
        return False

