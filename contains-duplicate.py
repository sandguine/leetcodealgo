# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 
# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Solution 1: sort the array first then find if the next one is equal to the current one.
# Time Complexity: depending on the default sorting algorithm

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = sorted(nums)
        
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                return True
        
        return False
        
 # Solution 2: to be continued
