#String Methods
#capitlize()
str1 = "hello world"
a= str1.capitalize()
print (a)

#casefold()
str2= "HELLO WORLD"
b= str2.casefold()
print (b)

#center()
str3 = "apple"
c = str3.center(20)
print(c)

#count()
d = str3.count("apple")
print(d)

#encode()
str4 = "Your Name is Stella"
e = str4.encode()
print(e)

#endswith()
f = str4.endswith(".")
print(f)

#expandtabs
str5 = "H\te\tl\tl\to"
g =  str5.expandtabs(2)
print(g)

#find()
str6 = "Hello, Welcome to Python world."
h = str6.find("world")
print(h)

#format
str7= "For only {price:.2f} dollars!"
print(str7.format(price = 63))

#index()
str8 = "Hello, welcome to my world."
i1=str8.index("welcome")
print(i1)

#isalnum()
str9 = "Company12"
i2= str9.isalnum()
print(i2)

#isaplha()
i3= str9.isalpha()
print(i3)
