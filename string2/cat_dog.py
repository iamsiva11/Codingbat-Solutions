"""
Return True if the string "cat" and "dog" 
appear the same number of times in the given string.

"""

def cat_dog(str):
	cat_count=0
	dog_count=0


	if(len(str))>=6:
		for i in range(len(str)):
			if(str[i]=='c' and str[i+1]=='a' and str[i+2]=='t'):
				cat_count+=1
			if(str[i]=='d' and str[i+1]=='o' and str[i+2]=='g'):
				dog_count+=1

	if(cat_count==dog_count):
		return True

	return False	


#Revised -1
def cat_dog(str):
	cat_count=0
	dog_count=0


	if(len(str))>=6:
		for i in range(len(str)-2):
			if(str[i]=='c' and str[i+1]=='a' and str[i+2]=='t'):
				cat_count+=1
			if(str[i]=='d' and str[i+1]=='o' and str[i+2]=='g'):
				dog_count+=1

  	if(cat_count>=1 and cat_count==dog_count):
		return True

	return False	

#Rev-2
def cat_dog(str):
	cat_count=0
	dog_count=0

	if(len(str))>=3:
		for i in range(len(str)-2):
			if(str[i]=='c' and str[i+1]=='a' and str[i+2]=='t'):
				cat_count+=1
			if(str[i]=='d' and str[i+1]=='o' and str[i+2]=='g'):
				dog_count+=1

	# print "cat count" + cat_count.str				
	# print "dog count" + str(dog_count)

	print cat_count , dog_count 
	# print dog_count 

  	if(cat_count>=1 and cat_count==dog_count):
		return True
		
	if(len(str)<3):
		return True

	return False		


print cat_dog('dog') # False	
print cat_dog('cat') # False	

print cat_dog('catdog') # True
print cat_dog('catcat') # False
print cat_dog('1cat1cadodog') #True	
print cat_dog('1cat1catdodogoodgodog') #True	