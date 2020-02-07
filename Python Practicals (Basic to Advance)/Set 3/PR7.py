sentence = 'Welcome to edunbox this program shows creation of sets and some of its functions'
words=sentence.split()
unique_words=set(words)

#creating set from list
print('\n creating set from list')
print(unique_words)


#defining set
a = {1,3} 
print(a)

#adding item in set
print('\n adding item in set')
a.add('Hello')
print(a)

#adding multiple items in set
print('\n adding multiple items in set')
a.update([1,2,3])
print(a)

#removing item from set
print('\n removing item from set')
a.discard(4)
print(a)

#poping item from set
print('\n poping item from set')
print(a.pop())

#clearing set
print('\n clearing set')
a.clear()
print(a)

s1 = {1,2,3,4}
s2 = {3,4,5,6}
#set union
print('\n Set Union')
print(s1 | s2)
print(s1.union(s2))

#set intersection
print('\n Set Intersection')
print(s1 & s2)
print(s1.intersection(s2))

#set difference
print('\n Set Difference')
print(s1 - s2)
print(s1.difference(s2))

#set symmetric difference
print('\n Set Symmetric Difference')
print(s1 ^ s2)
print(s1.symmetric_difference(s2))