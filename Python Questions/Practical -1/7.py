print("Practical-7")
print()


nums = input("Enter number(s): ").split(' ')
ans = []

for num in nums:
	factorial = 1
	for i in range(1, int(num) + 1):
		factorial = factorial * i

	ans.append(str(factorial))

print (','.join(ans))