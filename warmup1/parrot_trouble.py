#parrot_trouble

#We have a loud talking parrot.
#The "hour" parameter is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
#Return True if we are in trouble.

def parrot_trouble(talking, hour):
	#trouble 
	if(talking and (hour<7 or hour>20)):
		return True
	else :
		return False


print parrot_trouble(True, 6) # True
print parrot_trouble(True, 7) # False
print parrot_trouble(False, 6) # False