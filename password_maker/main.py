from random import randint

def getLetter(letterStr):
	letterIndex = randint(0,len(letterStr)-1)
	letter = letterStr[letterIndex:letterIndex+1]

	return letter

def getPassword():
	letters = "abcdefghijklmnoprstuvwxyz"
	numbers = "0123456789"
	symbols = "#$%&/()=¿?¡![]+*"
	password = ""

	i = 0
	while i < 10:
		choice = randint(1,3)
		#choice = 1
		#print("Choice: %s"%choice)

		if choice == 1:
			password += getLetter(letters)

		i += 1

	print(password)

def main():
	getPassword()



if __name__ == '__main__':
	main()