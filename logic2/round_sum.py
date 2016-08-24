"""
For this problem, we'll round an int value up to the next multiple of 10 
if its rightmost digit is 5 or more, so 15 rounds up to 20.
Alternately, round down to the previous multiple of 10 if its rightmost digit 
is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of
their rounded values. To avoid code repetition, write a separate helper "def round10(num):"
and call it 3 times. Write the helper entirely below and at the same indent level as 
round_sum().
"""

def round_sum(a, b, c):
	sum=round10(a)+round10(b)+round10(c)
	# print round10(a)
	# print round10(b)
	# print round10(c)
	return sum


# #Correct for more than half the tests

# def round10(num):
	
# 	new_num=0
# 	#Special case  (num is less than 10)
# 	if(num<5):
# 		return 0
# 	elif(5<=num<=10):
# 		return 10
# 	#when (num is greater than 10)	
# 	else:
# 		rem=(num%10)
# 		if(rem<5): #down
# 			new_num= (num/10)*10
# 		if(rem>5): #up
# 			new_num= ((num/10)*10 )+10
# 	return new_num		

			

def round10(num):
	
	#new_num=0
	#Special case  (num is less than 10)
	if(num<5):
		return 0
	if(5<=num<=10):
		return 10
	
	#when (num is greater than 10)	
	new_num=(num/10)*10
	rem=(num%10)
	# if(rem<5): #down
	# 	return new_num
	if(rem>=5): #up
		new_num+=10
		#return new_num
		#new_num= ((num/10)*10) + 10
	
	return new_num		

#test cases failed for these
print round_sum(45, 21, 30) #100- run 50
print round_sum(23, 24, 25) # 70	- run 40
print round_sum(25, 24, 25) # 80	- run 20


# print round_sum(16, 17, 18) #60
# print round_sum(12, 13, 14) # 30
# print round_sum(6, 4, 4) # 10

