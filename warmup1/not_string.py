
#9
#not_string

#Given a string, return a new string where "not " 
#has been added to the front. However, if the string
#already begins with "not", return the string unchanged.


def not_string(str):
	if str.startswith("not"):
		return str
	else:
		return "not " + str
  


print not_string('candy') #'not candy'
print not_string('x') # 'not x'
print not_string('not bad') #'not bad'



#Alternate solution from codingbat
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3
