#last2

#Given a string, return the count of the number of times that 
#a substring length 2 appears in the string and also as the
#last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring)

# str="string"
# print str[len(str)-2 : len(str)]

# def last2(str):
# 	count=0
# 	last2_str = str[len(str)-2 : len(str)]
# 	for i in range(len(str)):
# 		if str[i:i+2] == last2_str:
# 			count+=1
# 	return count	


#revised -1
def last2(str):
	count=0
	last2_str = str[len(str)-2 : len(str)]
	for i in range(len(str)-2):
		if str[i:i+2] == last2_str:
			count+=1
	return count		


#Solution-CodingBat

def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

# str= "string"
# print str[0:2]

# for i in range(len(str)):
# 	print i
# 	print str[i:i+2] 

# str= "string"
# print str[len(str)-2 : len(str)]

print last2('hixxhi') # 1
print last2('xaxxaxaxx') # 1
print last2('axxxaaxx') # 2 
"""
