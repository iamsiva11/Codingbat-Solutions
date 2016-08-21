"""
Given two strings, return True if
 either of the strings appears at the very
  end of the other string, ignoring upper/lower 
  case differences (in other words, the computation 
  	should not be "case sensitive"). 
  Note: s.lower() returns the lowercase version of a string.
"""

def end_other(a,b):
	a=a.lower()
	b=b.lower()
	small=''
	large=''
	if (len(a)<len(b)):
		small=a
		large=b
	else:
		small=b
		large=a
	
	if(large.find(small)>1):
		return True
	return False	


#revised-2	

print end_other('Hiabc', 'abc') # True
print end_other('AbC', 'HiaBc') # True
print end_other('abc', 'abXabc') # True


