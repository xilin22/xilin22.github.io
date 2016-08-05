from hashlib import *

finish = 0

loginDict = {}

def makeHash(Password):
	return sha256(Password.encode("utf-8")).hexdigest() 

def create_account(loginDict):
	user_name = input("Enter your username: ")
	password = input("Enter your password: ")
	hash_pass = makeHash(password) 
	loginDict[user_name] = hash_pass

def login(loginDict):
	user_name = input("Enter your username: ")
	password = input("Enter your password: ")
	hash_pass = makeHash(password) 
	if user_name not in loginDict:
		user_input = input("That account does not exist. Do you want us to make you a new account? (yes/no) ")
		if user_input == "yes":
			loginDict[user_name] = hash_pass
			print("Alright, your account has been created.")
		else:
			print("Bye")
	else:
		print("Success! You are logged in!")
		if user_name in loginDict and  loginDict[user_name] != hash_pass:
			print("Invalid Password. Please try Again.")



def prompt():
	input_1 = input("Would you like to create an account or login or leave?: ")
	if input_1 == "create":	
		create_account(loginDict)
	elif input_1 == "login":
		login(loginDict)

	elif input_1 == "leave":
		print("Bye")
		quit()
	else:
		print("Invalid command! Please try again.")	

while finish == 0:
	prompt()



# if I login
#	if my username does not exist in the dictionary, then prompt me to create an account
#	if my username does exist in the dictionary and I have the right password, tell me success!
# 	if my username does exist but it's the wrong password, tell me I'm intruder or that I got the password wrong

# stretch challenge: if username does exist and password is wrong, prompt 2 more times to enter password. if it's wrong all three times, tell me I'm an intruder

# loginDict[user_name] = hash_pass
	#if user_name not in loginDict:
		#user_name = input("Enter your username: ")