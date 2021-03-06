# Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.

#Correct for more than half the tests

def pos_neg(a, b, negative):
	if(negative):
		if(a<0 and b<0):
			return True
	else:
		if(a<0 or b<0):
			return True
		else:
			return False


#Revised Solution -1
		
def pos_neg(a, b, negative):
	if(negative):
		if(a<0 and b<0):
			return True
		else:
			return False
	else:
		if(a<0 and b<0):	
			return False
		elif (a<0 or b<0):
			return True


	
#Revised Solution -2

def pos_neg(a, b, negative):
	if(negative):
		if(a<0 and b<0):
			return True
		else:
			return False
	else:
		if(a<0 and b<0):	
			return False
		elif (a<0 or b<0):
			return True
		else:	
			return False


print pos_neg(1, -1, False) # True
print pos_neg(-1, 1, False) # True
print pos_neg(-4, -5, True) # True