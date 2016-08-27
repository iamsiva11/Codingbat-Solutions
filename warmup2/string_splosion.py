#Given a non-empty string like "Code" 
#return a string like "CCoCodCode".

# str="code"
# print str[:1]

# # for i in range(len(str)):
# # 	print i

def string_splosion(str):
	new_str=""
	for i in range(len(str)+1):
		new_str+=str[:i]
	return new_str


print string_splosion('Code') # 'CCoCodCode'
print string_splosion('abc') # 'aababc'
print string_splosion('ab') # 'aab'