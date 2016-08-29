
"""
Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending 
to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
"""

#Approach1				
def sum67(nums):
	#every 6  series will end with a 7 
	sum=0
	seen_6=False
	for i in range(len(nums)):
		if(nums[i] == 6):
			seen_6=True

		if(seen_6):
			#I need to ignore the indexx until i see a 7
			#i+=1
			# if(nums[i+1]==7):
			# 	#will not see the 6,7 sequence Again, so wil;l set the seen_6 flag false
			# 	seen_6=False
			# 	#i+=1
			#j=i
			for i in range(len(nums)):
				if(nums[i]==7):
					seen_6=False
					break

				# else:
				# 	continue						

					#break#/continue

		if(not seen_6):
			sum+=nums[i]		
			
		# else:
		# 	sum+=0
		# 	if(nums[i]is 7):
	return sum

#Approach2				
#getting the index of first 6 followed by a 7

#approach
#start 2 loops from 1 end , another loop from another end break 2 loops when they see 
#the respective trigger numbers

print sum67([1, 2, 2]) # 5
print sum67([1, 2, 2, 6, 99, 99, 7]) # 5
print sum67([1, 1, 6, 7, 2]) # 4
#print sum67([1, 1, 23,1, 6, 7, 2]) # 4
"""