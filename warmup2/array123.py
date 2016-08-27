#array123

#Given an array of ints, return True 
#if .. 1, 2, 3, .. appears in the array somewhere.


def array123(nums):
	if(len(nums)<1):
		return False

	for i in range(len(nums)-2):
		if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
			return True
	return False


#My soulution above and the alternate solutions are the same

print array123([1, 1, 2, 3, 1]) # True
print array123([1, 1, 2, 4, 1]) # False
print array123([1, 1, 2, 1, 2, 3]) # True

# nums = [1, 1, 2, 3, 1]
# for i in range(len(nums)-3):
# 	print nums[i]
# print nums[len(nums)-3]
# print nums[len(nums)-1]

"""

