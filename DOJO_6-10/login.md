

/wordle
This route takes you to wordle game
cookies 

login form
username testUser
password SecretPassword

When logging in create a cookie in the front end using some hash

secretHash JWT(username+password+random)

if the login is not right:
    return 405 your secretHash is rejected
else 
    return 200 your secretHash is stored in a sessions table maybe set a timeout



