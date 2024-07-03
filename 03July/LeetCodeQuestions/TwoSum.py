"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from Run_Time import time_function


def twoSum(nums, target):
    for num in nums:
        search_num = target - num
        if num == search_num:
            indices = [i for i in range(len(nums)) if nums[i] == search_num]
            if len(indices) == 2:
                return indices
        else:
            set_nums = set(nums)
            if search_num in set_nums:
                return [nums.index(num), nums.index(search_num)]


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
print(time_function(twoSum(nums, target)))
