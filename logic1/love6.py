"""
#7
The number 6 is a truly great number.
Given two int values, a and b, return True if either one is 6. 
Or if their sum or difference is 6. Note: the function abs(num) 
computes the absolute value of a number.
"""

def love6(a, b):
	if(a==6 or b==6):
		return True
	elif(abs(a-b)==6 or (a+b)==6):
		return True	
	return False  

print love6(6, 4) # True
print love6(4, 5) # False
print love6(1, 5) # True

