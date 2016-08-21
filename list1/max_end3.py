"""
# Given an array of ints length 3, figure out which 
# is larger between the first and last elements in the array,
# and set all the other elements to be that value. Return the changed array.
"""

def max_end3(nums):
	first=nums[0]
	last=nums[len(nums)-1]

	if(first>last):
		setnum=first
	else:
		setnum=last

	for i in range(3):
		nums[i]=setnum

	return nums	


print max_end3([1, 2, 3]) #[3, 3, 3]
print max_end3([11, 5, 9]) # [11, 11, 11]
print max_end3([2, 11, 3]) # [3, 3, 3]

