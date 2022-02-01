# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        number_deque = collections.deque(nums)
        reverse_sorted_squares = []
        while number_deque:
            left_square = number_deque[0] ** 2
            right_square = number_deque[-1] ** 2
            if left_square > right_square:
                reverse_sorted_squares.append(left_square)
                number_deque.popleft()
            else:
                reverse_sorted_squares.append(right_square)
                number_deque.pop()
        return reverse_sorted_squares[::-1]
