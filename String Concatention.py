#String Concatention
a="Hello"
b="World"
c=a+b
print(c)

#Another method
d=a+" "+b
print(d)

#String Formats- Python 3.6
e=5
str=f"What is the given number {e} "
print(str)

#Placeholders & Modifiers
price=630
a_str=f"Price of apple {price} dollars"
print(a_str)
b_str=f"Price of apple {price:.2f} dollars"
print(b_str)
c_str=f"Price of apple {2*5} dollars"
print(c_str)

#Escape Character
str1="We all are \"Good\" People"
print(str1)

#Single Quote
str2='It\'s alright.'
print(str2)

#Backslah
str3="This will insert one \\ (backslash)."
print(str3)

#New Line
str4="Welcome to\n'Python World!'"
print(str4)

#Carriage Return
str5="Hello\rWorld!"
print(str5)

#Tab
str6="Hello\tWorld!"
print(str6)

#Blankspace
str7="Hello \bWorld!"
print(str7)

#A backslash followed by three integers will result in a octal value
str8 = "\110\145\154\154\157"
print(str8)

#A backslash followed by an 'x' and a hex number represents a hex value:
str9 = "\x48\x65\x6c\x6c\x6f"
print(str9) 



