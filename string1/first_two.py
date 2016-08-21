# Given a string, return the string made of its first two chars, 
# so the String "Hello" yields "He". If the string is shorter than length 2,
# return whatever there is, so "X" yields "X", and the empty string 
# "" yields the empty string "".


def first_two(str):
	first2=str[:2]
	if len(str)<2:
		return str
	return first2	
  
print first_two('Hello') # 'He'
print first_two('abcdefg') # 'ab'
print first_two('ab') # 'ab'
print first_two('') # 'ab'