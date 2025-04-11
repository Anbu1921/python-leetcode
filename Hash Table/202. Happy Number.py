class Solution:
    def sumOfSquare(self, n: int) -> int:
        res = 0

        while n:
            rem = n % 10
            rem **= 2
            res += rem
            n = n // 10
        
        return res

    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquare(n)

            if n == 1:
                return True
        
        return False

        # Time: O(n)
        # Space: O(n)
