# Q-5 : Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order.

with open('test.txt','r') as f:
	for line in f:
		print(set(line.split()))