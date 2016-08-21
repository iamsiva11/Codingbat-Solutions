"""
Given 2 strings, a and b, return a string of the form 
short+long+short, with the shorter string on the outside
and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).
"""

def combo_string(a, b):
	short_str=""
	long_str=""
	if(len(a)<len(b)):
		short_str=a
		long_str=b
	else:
		short_str=b
		long_str=a

	return short_str+long_str+short_str	


print combo_string('Hello', 'hi') # 'hiHellohi'
print combo_string('hi', 'Hello') # 'hiHellohi'
print combo_string('aaa', 'b') # 'baaab'

