"""
Given a string, return a new string made of 3 copies 
of the last 2 chars of the original string. 
The string length will be at least 2.
"""


def extra_end(str):
	last2=str[-2:]
	return 3*last2
  

print extra_end('Hello') #'lololo'
print extra_end('ab') # 'ababab'
print extra_end('Hi') # 'HiHiHi'


