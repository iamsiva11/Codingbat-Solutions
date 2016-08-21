"""
Given an array of ints, return the sum of the first 2 elements in the array. 
If the array length is less than 2, just sum up the elements that exist, 
returning 0 if the array is length 0.
"""


def sum2(nums):
	sum=0

	if (len(nums)<1):
		return 0

	if (len(nums)<2):
		return nums[0]		

	if (len(nums)>=2):
		for i in range(2):
			sum+=nums[i]
	
	return sum


print sum2([1, 2, 3]) # 3
print sum2([1, 1]) # 2
print sum2([1, 1, 1, 1]) # 2
