'''
Write a python program that accept file name as input from the user. 
Open the file and count the number of times a character appears in the file.
'''


def letterCounter(fileName, letter):
	file = open(fileName, 'r')
	text = file.read()
	return text.count(letter)


if __name__ == "__main__":
    file_input = input('File Name: ')
    chars=input("Enter a char: ")
    print(f"Total number of {chars} is :  {letterCounter(file_input, chars)}")
    