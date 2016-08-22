"""
#9
Given a non-negative number "num", return True if num is within 2 
of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, 
so (7 % 5) is 2. See also: Introduction to Mod

"""

def near_ten(num):	
	from10=num%10
	
	if(from10>5):
		from10=(10-from10)

	if(from10<=2):
		return True
	else:
		return False
  

print near_ten(12) # True
print near_ten(17) # False
print near_ten(19) # True