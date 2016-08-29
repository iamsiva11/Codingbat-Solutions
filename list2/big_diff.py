
"""
Given an array length 1 or more of ints, 
return the difference between the largest
and smallest values in the array. Note: 
the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
"""

def big_diff(nums):	
	#Edge Cases
	if(len(nums)<1):
		return []

	if(len(nums)<2):
		return nums[0]

	if(len(nums)==2):
		#return min(nums[0],nums[1])	
		return abs(nums[0]-nums[1])	
	
	max_val=0
	min_val=0
	#block for Minimum value
	if (len(nums)>2):
		now_min=nums[0]
		now_min=min(nums[0],nums[1])
		#i=2
		for i in range(len(nums)):
			#i=2			
			if nums[i]<now_min:
				now_min=nums[i]
				#print now_min
		min_val=now_min
	
	
	# if (len(nums)>2):
	# #block for Maaximum value 	
	 	now_max=nums[0]
		now_max=max(nums[0],nums[1])
		for i in range(len(nums)):
			#i=2
			if nums[i]>now_max:
				now_max=nums[i]
				#print now_max
		max_val=now_max

	# print max_val
	# print min_val		
	return max_val-min_val

#comments 
#Should optimise unnecesary comparing of first 2 indexes in the loop	


print big_diff([10, 3, 5, 6]) # 7
print big_diff([7, 2, 10, 9]) # 8
print big_diff([2, 10, 7, 2]) # 8
print big_diff([3, 9]) 