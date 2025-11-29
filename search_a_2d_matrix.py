# https://leetcode.com/problems/search-a-2d-matrix-ii/

# brutforce O(m*n)
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # apply binary search on rows
        # same can be done on columns using 
        # for i in range(n)
            # low, high = 0, m - 1
        for i in range(m):
            low, high = 0, n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return n
        
solution = Solution()
print(solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))

# target = 5
# output = true
