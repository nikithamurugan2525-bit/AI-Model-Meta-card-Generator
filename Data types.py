# python numeric Data types (Integer,Float,Complex)

x = 10
print(type(x)) # int type
y = 25.00
print(type(y)) #floating point representation
z = 5 + 4j
print(type(z))

# Python Sequence data type (String,List,Tuple)
# 1.string :
str = input("Enter the word:")
print(type(str)) # type of str
# accessing the string
print(str[-1])
print(str[0])
print(str[3])

# 2.List

a = [] # empty list

b = [1,2.7,3,4.0,5] # list with numeric values
print(b)
c = ["list","tuple","set","array"]
print(c) # list with string values

# Boolean type
print(type(True))
print(type(False))

A = int(input("Enter the number either 0 or 1 :"))
if A == 1 :
    print("1 is True")
else :
    print("0 is False")

# truthy and Falsy

print(bool(7))       # non zero number(true)
print(bool(0))      # False
print(bool([1,2,3])) # non empty list(True)
print(bool([]))     # False
print(bool(None)) # false


# set Data types:
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = {"Geeks", "For", "Geeks"}
print("Set with the use of List: ", s2)