from random import randint

def getLetter() -> str:
	letters = "abcdefghijklmnoprstuvwxyz"
	isUpper = randint(0,1)
	letterIndex = randint(0,len(letters)-1)
	letter = letters[letterIndex:letterIndex+1]

	if isUpper:
		return letter.upper()
	else:
		return letter	
		
	print("Is Upper: %d"%isUpper)
	
def getNumber() -> str:
	numbers = "0123456789"
	numberIndex = randint(0,len(numbers)-1)
	number = numbers[numberIndex:numberIndex+1]
	return number

def getSymbol() -> str:
	symbols = "#$%&/()=¿?¡![]+*"
	symbolIndex = randint(0,len(symbols)-1)
	symbol = symbols[symbolIndex:symbolIndex+1]
	return symbol


def getPassword():
	while True:
		try:
			passwordLength = int(input("Password Length: "))
		except:
			print("You Gave A Wrong Value.")
		else:
			break
			
	password = ""

	i = 0
	while i < passwordLength:
		choice = randint(1,3)
		#choice = 1
		#print("Choice: %s"%choice)

		if choice == 1:
			password += getLetter()
		elif choice == 2:
			password += getNumber()
		elif choice == 3:
			password += getSymbol()

		i += 1

	print("Password: %s\nLength: %s"%(password,len(password)))

def main():
	getPassword()



if __name__ == '__main__':
	main()