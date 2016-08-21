# Given a string of even length, return the first half. 
# So the string "WooHoo" yields "Woo".


def first_half(str):
	halflen=len(str)/2
	return str[:halflen]

 
print first_half('WooHoo') # 'Woo'
print first_half('HelloThere') # 'Hello'
print first_half('abcdef') # 'abc'