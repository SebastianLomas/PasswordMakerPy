from random import randint

def getLetter(letterStr):
	isUpper = randint(0,1)
	letterIndex = randint(0,len(letterStr)-1)
	letter = letterStr[letterIndex:letterIndex+1]

	if isUpper:
		return letter.upper()
	else:
		return letter	
		
	print("Is Upper: %d"%isUpper)
	
def getNumber(numberStr : str) -> str:
	numberIndex = randint(0,len(numberStr)-1)
	number = numberStr[numberIndex:numberIndex+1]
	return number

def getSymbol(symbolStr : str) -> str:
	symbolIndex = randint(0,len(symbolStr)-1)
	symbol = symbolStr[symbolIndex:symbolIndex+1]
	return symbol


def getPassword():
	while True:
		try:
			passwordLength = int(input("Password Length: "))
		except:
			print("You Gave A Wrong Value.")
		else:
			break
			
	letters = "abcdefghijklmnoprstuvwxyz"
	numbers = "0123456789"
	symbols = "#$%&/()=¿?¡![]+*"
	password = ""

	i = 0
	while i < passwordLength:
		choice = randint(1,3)
		#choice = 1
		#print("Choice: %s"%choice)

		if choice == 1:
			password += getLetter(letters)
		elif choice == 2:
			password += getNumber(numbers)
		elif choice == 3:
			password += getSymbol(symbols)

		i += 1

	print("Password: %s\nLength: %s"%(password,len(password)))

def main():
	getPassword()



if __name__ == '__main__':
	main()