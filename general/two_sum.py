"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum(nums, target):
    seen = {}
        
    for key, value in enumerate(nums):
        rem = target - value 
        if rem in seen:
            return [key, seen[rem]]
        seen[value] = key

def twoSum2(nums, target):
    low, high = 0, len(nums) - 1

    while(low < high):
        _sum = nums[low] + nums[high]
        if _sum == target:
            return [low, high]
        elif _sum < target:
            low += 1
        else:
            high -= 1


# Given 
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
print(twoSum2(nums, target))