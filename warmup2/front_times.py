#Given a string and a non-negative int n,
#we'll say that the front of the string is the first 3 chars,
#or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
	string_front=3
	if len(str)<3:
		string_front=len(str)
	return n* str[:string_front]	


#Alternate Solution
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result


print front_times('Chocolate', 2) #'ChoCho'
print front_times('Chocolate', 3) # 'ChoChoCho'
print front_times('Abc', 3) # 'AbcAbcAbc'