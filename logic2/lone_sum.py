"""
Given 3 int values, a b c, return their sum. However, 
if one of the values is the same as another of the values, 
it does not count towards the sum.
"""

def lone_sum(a, b, c):
	list_three=[a]
	#list_three.append(b)
	#list_three.remove(a)
	#rint list_three

	#print sum(list_three)

	prev_remov=0
	if b not in list_three:
		list_three.append(b)
	else:
		prev_remov=b
		list_three.remove(b)


	if c not in list_three:
		if c == prev_remov:
			return sum(list_three)
		list_three.append(c)
	else:
		list_three.remove(c)


	return sum(list_three)


#(or a simple alternative soluton without lists)	
			

print lone_sum(1, 2, 3) # 6
print lone_sum(3, 2, 3) # 2
print lone_sum(3, 3, 3) # 0
