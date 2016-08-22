"""
#1
When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
Unless it is the weekend, in which case there is no upper bound on the number of cigars.
 Return True if the party with the given values is successful, or False otherwise.
"""

def cigar_party(cigars, is_weekend):
	lowerbound=40
	upperbound=60
	if(40<=cigars<=60 and not is_weekend):
		return True
	elif (40<=cigars and is_weekend):
		return True	
  	return False

print cigar_party(30, False) # False
print cigar_party(50, False) # True
print cigar_party(70, True) # True


