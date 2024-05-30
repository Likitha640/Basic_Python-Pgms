#Python Lists
list1 = ["python", "java", "C#"]
print(list1)

#Duplicate
list2 = ["python", "java", "C#", "python", "java"]
print(list2)

#length of the string
print(len(list1))

#List with Data types
list3 = ["apple", "banana", "cherry"]
list4 = [6, 30, 16, 21, 13]
list5 = [True, False, False]
print(list3)
print(list4)
print(list5)

list6 = ["abc", 6, True, 30, "good"]
print(list6)
print(len(list6))
print(type(list6))

#list() Constructor
list7 = list(("apple", "banana", "cherry","strawberry","orange","mango","grapes")) 
print(list7)

#Access List Items
list8=["apple", "banana", "cherry","strawberry","orange","mango","grapes"]
print(list8[1])
print(list8[-1])
print(list8[2:5])
print(list8[-4:-3])
print(list8[:4])
print(list8[2:])
if "apple" in list8:
  print("Yes, 'apple' is in the fruits list")

list8[1] = "blackcurrant"
print(list8)

list8[1:2] = ["kiwi", "watermelon"]
print(list8)

list9 = ["ABC", "LVR", "PQR"]
list9.insert(2, "KIM")
print(list9)

list9.append("KTH")
print(list9)

list9.insert(1, "VLI")
print(list9)

list10=["AA","BB","CC"]
list11=["XX","YY","ZZ"]
list10.extend(list11)
print(list10)