"""
Return True if the given string contains 
an appearance of "xyz" where the xyz is not 
directly preceeded by a period (.).
So "xxyz" counts but "x.xyz" does not.
"""

def xyz_there(str):
	#base_condition= (str[i]=='x' and str[i+1]=='y' and str[i+2]=='z')
	for i in range(len(str)):
		if(str[i]=='x' and str[i+1]=='y' and str[i+2]=='z' and str[i-1]=='.'):
				return False
		if(str[i]=='x' and str[i+1]=='y' and str[i+2]=='z'):
			return True		
		
	return False		


#rev-2

def xyz_there(str):
	if(len(str)>3):
	  	#base_condition= (str[i]=='x' and str[i+1]=='y' and str[i+2]=='z')
	  	for i in range(len(str)):
	  		if i>=1:	
	  			if(str[i]=='x' and str[i+1]=='y' and str[i+2]=='z' and str[i-1]=='.'):
	  					return False
	  		if(str[i]=='x' and str[i+1]=='y' and str[i+2]=='z'):
	  				return True		
	  			
	return False			


print xyz_there('abcxyz') # True
print xyz_there('abc.xyz') # False
print xyz_there('xyz.abc') # True
