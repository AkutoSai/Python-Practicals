import statistics

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
print()
        


# calculate the median of the given list
def median(number_list):
    length = len(number_list)
    if((length%2)==0):
        first = number_list[int((length/2))-1]
        second = number_list[int(length/2)]
        i =(first+second)/2
        return i
    else:
        return number_list[length//2]
        

# calculate the mode of the given list
def mode(number_list):
    return statistics.mode(number_list)

# calculate the average of list
def mean(number_list):
    return statistics.mean(number_list)
    

print("Median of the given list is:", median(number_list))
print()
print("Median of the given list is:", mean(number_list))
print()
print("Median of the given list is:", mode(number_list))
