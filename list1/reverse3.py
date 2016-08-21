"""
Given an array of ints length 3, return a new array 
with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
"""


# nums = [12,2,3,45]
# print nums[0:len(nums)]
# print nums[-1:]


def reverse3(nums):
  	iter=len(nums)-1
	new_list=[]
	for i in range(len(nums)):
		new_list.append(nums[iter])
		iter=iter-1
	return new_list


# def reverse3(nums):
# 	return nums[len(nums):]
  
print reverse3([1, 2, 3]) # [3, 2, 1]
print reverse3([5, 11, 9]) # [9, 11, 5]
print reverse3([7, 0, 0]) # [0, 0, 7]

