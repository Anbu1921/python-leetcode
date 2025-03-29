class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    t = m * n
    l = 0
    r = t - 1

    while l <= r:
      M = l + ((r - l) // 2)
      i = M // n
      j = M % n

      mid_num = matrix[i][j]

      if mid_num < target:
        l = M + 1
      elif mid_num > target:
        r = M - 1
      else:
        return True
        
    return False

      # Time: O(log n)
      # Space: O(1)