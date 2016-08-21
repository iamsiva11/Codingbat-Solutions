"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""


def count_hi(str):
	count=0
	for i in range(len(str)):		
		if(str[i]=='h' and str[i+1]=='i'):
			count+=1

	return count	


#Revised 2
def count_hi(str):
	count=0
	if(len(str)<2):
		return 0
	for i in range(len(str)):		
		if(str[i]=='h' and str[i+1]=='i'):
			count+=1

	return count	


print count_hi('abc hi ho') # 1
print count_hi('ABChi hi') # 2
print count_hi('hihi') # 2
  

