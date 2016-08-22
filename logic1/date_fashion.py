
"""
#2
# You and your date are trying to get a table at a restaurant. 
# The parameter "you" is the stylishness of your clothes, in the range 0..10, 
# and "date" is the stylishness of your dates clothes. The result getting the 
# table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you 
# is very stylish, 8 or more, then the result is 2 (yes). With the exception that 
# if either of you has style of 2 or less, then the result is 0 (no). 
# Otherwise the result is 1 (maybe).
"""

# def date_fashion(you, date):
# 	if(you>=8 or date>=8):
# 		return 2#"yes"
# 	elif(you<=2 or date<=2):	
# 		return 0#no
# 	return 1	


# def date_fashion(you, date):
# 	if(you>=8 or date>=8 and not (you<=2 or date<=2)):
# 		return 2
# 	elif(you>=8 or date>=8 and (you<=2 or date<=2)):
# 		return 0
# 	return 1	


def date_fashion(you, date):
	#if(you>=8 and date<=2 or (date>=8 and you<=2) ):
	if(you<=2 or date<=2):
		return 0
	# elif(you<8 or date<8 and (you<=2 or date<=2)):
	# 	return 0
	elif(you>=8 and date>=3 or (date>=8 and you>=3) ):		
		return 2
	return 1	


#What are he possible conditions for them to reject a invitaion for a place
#When either of them score os <=2
#write the possible , cut off conditions and  solve the problem, it gets easier

#8,2 comparision for you,date,

print date_fashion(5, 10) # 2
print date_fashion(5, 2) # 0
print date_fashion(5, 5) # 1
print date_fashion(2, 10) # 2
print date_fashion(10, 2) #0	#2	
print date_fashion(2, 9) #0 	#2


