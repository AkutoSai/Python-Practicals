print("Practical-6")
print()

#line=""

for x in range(5000, 5999):
  if (x%7)==0:
    y=x/5.0
    if (y%5)!=0:
        #line = line+str(x)+","
        print (str(x)+",")
        #print(line)