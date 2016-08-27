
#Given an array of ints, return True if one of the first 4 
#elements in the array is a 9. The array length may be less than 4.

# def array_front9(nums):
# # 	# if len(nums)<4:
# # 	# 	return False
# 	 for i in range(4):
# 		if nums[i]==9:
# 			return True		
# 		 else:
# 		 	return False	



#Revised 2
def array_front9(nums):
 	 if len(nums)<4:
 	 	return False
	 for i in range(4):
		if nums[i]==9:
			return True		
		if i==3:
			return False

#Revised-2 		

def array_front9(nums):
	array_len=4
	if len(nums)<4:
 	 	array_len=len(nums)
	for i in range(array_len):
		if nums[i]==9:
			return True		
		if i==3:
			return False

#Revised-3
def array_front9(nums):
	array_len=4
	if len(nums)<4:
 	 	array_len=len(nums)
	for i in range(array_len):
		if nums[i]==9:
			return True		
		if i==array_len-1:
			return False


#Revised-4
def array_front9(nums):
	array_len=4
	if len(nums)<1:
		return False

	if len(nums)<4:
 	 	array_len=len(nums)

	for i in range(array_len):
		if nums[i]==9:
			return True		
		if i==array_len-1:
			return False



#Solution:
def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False


# arr=[1, 2, 9, 3, 4]
# for i in range(4):
# 	if arr[i]==9:
# 		print True
# 	else:
# 		print False	


print array_front9([1, 1, 1, 9]) # True
print array_front9([1, 2, 9, 3, 4]) # True
print array_front9([1, 2, 3, 4, 9]) # False
print array_front9([1, 2, 3, 4, 5]) # False

