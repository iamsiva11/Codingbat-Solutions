

"""
Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive 
-- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and 
returns that value fixed for the teen rule. In this way, you avoid repeating 
the teen code 3 times (i.e. "decomposition"). Define the helper below and at 
the same indent level as the main no_teen_sum().


def no_teen_sum(a, b, c):

	sum=0
	sum=fix_teen(a)+fix_teen(b)+fix_teen(c)
	return sum


# def fix_teen(n):
# 	if (13<=n<=19):
# 		if(n!=15 or n!=16):
# 			return 0
# 	return n		

# def fix_teen(n):
# 	if (13<=n<=19):

# 		if(n!=15 or n!=16):
# 			return 0
# 		else: 	
# 			return n
# 	return n	


def fix_teen(n):
	if (13<=n<=19 and (n!=15 and n!=16)):
			return 0		
	return n	

(or)	

def fix_teen(n):
	if (13<=n<=14 or 17<=n<=17):
			return 0		
	return n	


print no_teen_sum(1, 2, 3) #6
print no_teen_sum(2, 13, 1) #3
print no_teen_sum(2, 1, 14) #3
print no_teen_sum(2, 1, 15) #18


"""