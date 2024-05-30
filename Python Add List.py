#Add Lists Items
list1 = ["python", "java", "C#"]
list2 = ("C programming", "HTML")
list1.extend(list2)
print(list1)

#Remove items
list1.remove("java")
print(list1)

list1.pop(1)
print(list1)

list1.pop()
print(list1)

list1.clear()
print(list1)

#Loop Lists
list3 = ["apple", "banana", "cherry"]
for x in list3:
  print(x)

#Loop with range
for i in range(len(list3)):
  print(list3[i])

#While Loop
list4 = ["AA","BB","CC","DD","EE"]
i = 0
while i < len(list4):
  print(list4[i])
  i = i + 1

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list5 = []

for x in fruits:
  if "a" in x:
      list5.append(x)

print(list5)

#Sort 