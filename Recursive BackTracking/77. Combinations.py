class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return 
            
            left = x
            still_need = k - len(sol)
            if left > still_need:
                backtrack(x - 1)
            
            sol.append(x)
            backtrack(x - 1)
            sol.pop()
        
        backtrack(n)
        return res
        # Time: O(N choose K)
        # Space: O(N)