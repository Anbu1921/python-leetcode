class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        ans, sol = [], []
        n = len(digits)

        letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}

        def backtrack(i=0):
            if i == n:
                ans.append(''.join(sol))
                return 
            
            for letter in letter_map[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return ans
        # Time: O(n * 4**n)
        # Space: O(n)
