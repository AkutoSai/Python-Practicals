# Q-3 : Write a program to convert each decimal number given in list to a fixed size binary
#		and generate a dictionary containing binary value as key and decimal number as
#		value.

def decToBin(nlist):
	lst = list()
	lst2 = list()
	dic = dict()
	for i in nlist:
		while i//2 !=0:
			lst.append(i%2)
			i=i/2
		lst.append(1)
		lst.reverse()
		b = map(str,lst)
		str1 = ''.join(b)
		lst2.append(str1)
		lst[:] = []

	for i in nlist:
		for y in range(len(lst2)-1):
			dic[i]=lst2[y]
	print(dic)

if __name__ == '__main__':
	lis =[15,14,4,2]
	decToBin(lis)