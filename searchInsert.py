# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Solution 1:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            
            mid = (left+right)//2
            #print("left: ", left, " right: ", right, " nums[mid]: ", nums[mid])
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]: # on the left of the list
                right = mid - 1
            else:
                left = mid + 1
            
        return left

# Solution 2:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return sorted(nums + [target]).index(target)
