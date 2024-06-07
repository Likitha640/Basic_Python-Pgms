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
