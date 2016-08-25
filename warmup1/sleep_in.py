
#The parameter weekday is True if it is a weekday, 
#and the parameter vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

#Weeday,vacation

# def sleep_in(weekday, vacation):
# 	if weekday:
# 		print "hi"
# 	else:
# 		print "ho"

#ti=hink throught the first principles
#when i can sleep
# i can sleep in vacation or not weekday

def sleep_in(weekday, vacation):
	if (not weekday) or vacation:
		return True
	else:
		return False


# def sleep_in(weekday, vacation):
# 	if weekday or (not vacation):
# 		print "False"
# 		return False
# 	elif (not weekday) or vacation:
# 		print "True"
# 		return True
		
print sleep_in(False, False) # True
print sleep_in(True, False) # False
print sleep_in(False, True) # True


