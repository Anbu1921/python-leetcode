class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        results = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left])
                left += 1
            else:
                result.append(nums[right])
                right += 1
        
        result.reverse()

        return result

        # Time: O(n)
        # Space: O(1)