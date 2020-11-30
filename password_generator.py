"""
This python code generates a random password of size 16. The other requirements for the random password are the following:
Minimum Number of Upper Case Letters: 1
Minimum Number of Lower Case Letters: 1
Minimum Number of Digits: 3
"""

import string
import secrets

characters= string.ascii_uppercase + string.ascii_lowercase + string.digits 

#to check the conditions, we start an while loop set to the default value of true

while True: 
    #we first create the password using the secret library and a for loop
    password= "".join(secrets.choice(characters) for i in range(16))
    
    #checks whether the conditions are fullfilled    
    if (any(c.islower() for c in password) 
        and any(c.isupper()for c in password)
        and sum(c.isdigit()for c in password)>=4):
        break #breaks the loop when conditions are met

print (password)

#end of program

