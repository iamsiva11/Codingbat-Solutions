
#string_match

#Given 2 strings, a and b, return the number of the positions
#where they contain the same length 2 substring. So "xxcaazz" and
#"xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
	count=0
	if(len(a)<2 or len(b)<2):
		return 0

	str_len=0	
	if(len(a)>len(b)):
		str_len=len(b) 	
	else:
		str_len=len(a) 		

	for i in range(str_len-1):
		if(a[i]==b[i] and a[i+1]==b[i+1]):
			count+=1
	return count		

#Solution:

def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count	


print string_match('xxcaazz', 'xxbaaz') # 3
print string_match('abc', 'abc') # 2
print string_match('abc', 'axc') # 0


