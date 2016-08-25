"""
#11
#Given a string, return a new string where 
#the first and last chars have been exchanged.

# def front_back(str):
# 	str[0] = str[len(str)-1], str[len(str)-1] = str[0]
# 	return str

def front_back(str):
	if len(str)>1:
		return str[len(str)-1] + str[1:len(str)-1] + str[0]
	else:
		return str


# Alternate Solution:
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  # last + mid + first
  return str[len(str)-1] + mid + str[0]


# str="kappas"
# str[0]=str[len(str)-1]  

print front_back('code') # eodc
print front_back('a') # a
print front_back('ab') # ba
