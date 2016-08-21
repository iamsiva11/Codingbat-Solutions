"""
Given an array of ints length 3, return an array with 
the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""


# def rotate_left3(nums):
# 	return nums[1:len(nums)]+nums[0]

#ver2
def rotate_left3(nums):

	new_list=nums[1:len(nums)]
	#print new_list
	new_list.append(nums[0])
	#print new_list
	return new_list

#rotate_left3([1, 2, 3]) #[2, 3, 1]

print rotate_left3([1, 2, 3]) #[2, 3, 1]
print rotate_left3([5, 11, 9])# [11, 9, 5]
print rotate_left3([7, 0, 0]) # [0, 0, 7]

