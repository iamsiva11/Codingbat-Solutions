#Given a non-empty string and an int n, 
#return a new string where the char at index n has been removed.
#The value of n will be a valid index of a char in the original string 
#(i.e. n will be in the range 0..len(str)-1 inclusive).

# #kitten
# str = "kitten"

# # print str[:2]
# # print str[:1]
# n=0
# print str[:n]+ str[n+1:len(str)]

def missing_char(str, n):
	return str[:n]+ str[n+1:len(str)]
 

print missing_char('kitten', 1) # 'ktten'
print missing_char('kitten', 0) # 'itten'
print missing_char('kitten', 4) # 'kittn'



