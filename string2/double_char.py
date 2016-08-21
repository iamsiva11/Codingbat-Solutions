
"""
Given a string, return a string where for 
every char in the original, there are two chars.
"""


def double_char(str):
	# for i in str:
	# 	print i+i,
	newstr=""

	for i in range(len(str)):
		str1=str[i]*2
		newstr+=str1
	return newstr	
  	
  
print double_char('The') # 'TThhee'
print double_char('AAbb') # 'AAAAbbbb'
# double_char('Hi-There') # 'HHii--TThheerree'

