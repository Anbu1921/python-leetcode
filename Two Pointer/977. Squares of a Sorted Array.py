class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        results = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                results.append(nums[left] ** 2)
                left += 1
            else:
                results.append(nums[right] ** 2)
                right -= 1
        
        results.reverse()

        return results

        # Time: O(n)
        # Space: O(1)
