# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


# Solution 1: updating one comparing point in the middle.
# Time Complexity: 	Θ(log(n))
# Memory Complexity: 	Θ(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find middle index
        left = 0
        right = len(nums)-1
    
        while True:
            
            mid = floor((left+right)/2)
            #print("left: ", left, " right: ", right, " nums[mid]: ", nums[mid])
            
            if target == nums[mid]:
                return mid
            if left >= right:
                return -1
            elif target > nums[mid]: # on the right of the list
                left = mid + 1
            elif target < nums[mid]: # on the left of the list
                right = mid - 1

# Solution 2: two pointers. Similar to solution 1.
# Time Complexity: 	Θ(log(n))
# Memory Complexity: 	Θ(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = 0
        left = len(nums)-1
        
        while right <= left:
            
            # check right
            if nums[right] == target:
                return right
            else:
                right+=1
            
            # check left
            if nums[left] == target:
                return left
            else:
                left-=1
        
        return -1
