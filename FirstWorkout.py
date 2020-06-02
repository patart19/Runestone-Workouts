# List Methods

#adding the number 7 to the end of the list.
y = [1, 2, 3, 4, 5]
y.append(7)
print(y)

#reverse the order of the list
y.reverse()
print(y)

#putting the list back in order
y.sort()

#adding the number 6 to the 5th position in the list.
y.insert(5, 6)
print(y)

#Create a list, myList, that includes 0 and 100 (non inclusive).
myList = range(0,100)
print(myList)

#Create a list, AnotherList, that includes 0 to 101 (non inclusive) in increments
#of 20
AnotherList = range(0, 101, 20)
print(AnotherList)
