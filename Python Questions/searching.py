def linear_s(num_list,number):
    for i in range(0,len(num_list)-1):
        if num_list[i] == number:
            return i
    return False

def binary_s(num_list,number):
    num_list.sort()
    print("Sorted list is:",num_list)
    
    if(len(num_list)%2==0):
        i=len(num_list)//2
        
        if(number>num_list[i]):
            binary_s(num_list[i:],number)
        else:
            binary_s(num_list[:i],number)
    else:
        i=(len(num_list)//2)+1
        
        if(number == num_list[i]):
            return i
        if (number>num_list[i]):
            binary_s(num_list[i:],number)
        if (number<num_list[i]):
            binary_s(num_list[:i],number)
    return False

      
print("//////Enter set of numbers//////")
print("/////To stop entering number enter */////")
var = True
number_list = []

while (var == True):
    num = input("Enter number : ")
    if(num =='*'):
        var = False
        break
    else :
        num = int(num)
        number_list.append(num)
print("/////your input LIST is :")
print(number_list)
num=int(input("Input number you want to search in list:"))

print("Your searched result is on" ,binary_s(number_list,num),"this position in list")
