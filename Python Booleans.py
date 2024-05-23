#Python Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

#if loop
a = 300
b = 64

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#Evaluate Values & Variables - True
print(bool("Hello"))
print(bool(15))

x = "Hello World"
y = 50
print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple","banana","cherry"]))

#Booleans - False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Using Functions 
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

#Functions
def myFunction() :
  return True

if myFunction():
  print("CORRECT")
else:
  print("INCORRECT")

#Check oject integer or not
a = 200
print(isinstance(a, int))
print(isinstance(a,float))