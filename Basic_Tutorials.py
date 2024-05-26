#Output Statement
print("Basic Python Learnings")

"""This is a
multiline statement"""
print("Python is awesome")

#Python Variables
x=5
y="John"
print(x)
print(y)

#Specify data type
a=str(3)
b=int(3)
c=float(3)
print(a)
print(b)
print(c)

#Get Type
d=5
print(type(d))

#Unpack Collections
cars=["BMW","Jaguar","Genesis"]
g,h,i=cars
print(g)
print(h)
print(i)

#Output variables
j="Python is a"
h="high-level"
k="programming language"
print(j,h,k)
print(j+ h + k)

#Global Variable - Type 1
l="good"
def myfunc1():
    print("Python is "+l)
    myfunc1()
print(l)

#Global Variable - Type 2
m="perfect"
def myfunc2():
    n="too awesome"
    print("Python is "+n)
myfunc2()
print(m)
