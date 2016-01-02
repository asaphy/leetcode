''''
1. Two Sum My Submissions Question

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
def twoSum(self, nums, target):
        #return false if lenght of input array is 1 or less
    if len(nums) <= 1:
        return false
    dict = {}
    #iterate through input array
    for i in range (0,len(nums)):
            #target value is equal to index i of the input array and a previous value
        if nums[i] in dict:
            return [dict[nums[i]], i+1]
        else:
                #add value that we need to sum up to the target into dictionary
            dict[target - nums[i]] = i + 1