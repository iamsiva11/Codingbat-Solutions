

#4
#diff21
#Given an int n, return the absolute difference
#between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
	#if abs(n-21)>21:
	if n>21:
		return 2*abs(n-21)
	else:
		return abs(n-21)
 
print diff21(19) #2
print diff21(10) # 11
print diff21(21) # 0

