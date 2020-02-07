# Q-2 : Write a program that allows the user to navigate the lines of text in a file. The
#	program should prompt the user for a filename and input the lines of text into a
#	list. The program then enters a loop in which it prints the number of lines in the
#	file and prompts the user for a line number. Actual line numbers range from 1 to
#	the number of lines in the file. If the input is 0, the program quits. Otherwise, the
#	program prints the line associated with that number.

def filefn():
	f = open("test.txt","w+")
	for i in range(10):
		f.Write("This is line %d\r\n" %(i+1))

	f.close()

	fin = open("test.txt","r")
	prt = "y"
	lines=fin.readlines()
	while prt != 'n':
		n = int(input("Enter the line number you want to print: "))
		print(lines[n])
		prt = input("Want to print any other linr? y or n: ")

	fin.close()

if __name__ == "__main__":
	filefn()