class Solution(object):
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