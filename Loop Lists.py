#Lists
#Loop through a List
list1 = ["apple", "banana", "cherry"]
for x in list1:
  print(x)
  
#Loop through the INdex Numbers
for i in range(len(list1)):
  print(list1[i])

#while loop
i = 0
while i < len(list1):
  print(list1[i])
  i = i + 1
  
#Sort Descending
list1.sort(reverse = True)
print(list1)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

list1 = [100, 50, 65, 82, 23]
list1.sort(key = myfunc)
print(list1)

#Case Insensitive Sort
list2 = ["AA", "CC", "BB", "DD"]
list3 = ["apple", "Orange", "Kiwi", "cherry"]
list2.sort()
list3.sort(key = str.lower)
print(list2)
print(list3)

list3.reverse()
print(list3)


#Copy of List - Method 1
mylist1 = list1.copy()
print(mylist1)

#Copy of List - Method 1
mylist2 = list(list1)
print(mylist2)

#Join Lists - Method 1
list3 = ["a", "b", "c"]
list4 = [1, 2, 3]

list5 = list3 + list4
print(list5)

#Join Lists - Method 2
for x in list4:
  list3.append(x)

print(list3)

