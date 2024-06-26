tuple1 = ("AA", "BB", "CC")
print(tuple1)
print(len(tuple1))

tuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple2)

#Create Tuple With One Item
tuple3 = ("apple",)
print(type(tuple3))

#NOT a tuple
tuple4 = ("apple")
print(type(tuple4))

tuple5 = ("abc", 34, True, 40, "male")
print(tuple5)

tuple6 = tuple(("apple", "banana", "cherry")) 
print(tuple6)

#Tuple Access Items
tuple7 = ("AA", "CC", "BB", "KK","LL","TT")
print(tuple7[1])
print(tuple7[-1])
print(tuple7[2:5])
print(tuple7[-2:-1])
print(tuple7[2:])
print(tuple7[:4])

#Update Tuples
x1 = ("RAM", "CPU", "ROM")
x2 = list(x1)
x2[1] = "UPS"
x1 = tuple(x2)
print(x1)

x3 = list(x1)
x3.append("ML")
x3 = tuple(x3)
print(x3)

#Unpack Tuples
colors = ("C1", "C2", "C3")
(green, yellow, red) = colors

print(green)
print(yellow)
print(red)

(green, yellow, *red) = colors
print(green)
print(yellow)
print(red)

(green, *tropic, red) = colors
print(green)
print(tropic)
print(red)

#Loop Through Tuples
tuple1 = ("JAVA", "C++", "Python")
for x4 in tuple1:
  print(x4)

#Loop Through Index Numbers
for i in range(len(tuple1)):
  print(tuple1[i])

#Using while loop
i1 = 0
while i1 < len(tuple1):
  print(tuple1[i1])
  i1 = i1 + 1

#Join Tuples
T1 = ("a", "b" , "c")
T2 = (1, 2, 3)
T3 = T1 + T2
print(T3)

fruits = ("ABC", "EFG", "XYZ")
T4 = fruits * 2
print(T4)

#Tuple Methods
T5 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x4 = T5.count(5)
print(x4)

x5 = T5.index(8)
print(x5)

