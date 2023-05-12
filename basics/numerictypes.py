#numeric datatypes
a=1
b=2
c=3
print(a,b,c)
print(type(a),type(b),type(c))

#float datatypes
x=3.1
y=7.9
z=203.0
print(type(x),type(y),type(z))

#complex datatypes
d = (3 + 7j)
print(type(d))

#Binary datatypes
e = 0B1010
print(e)

#Hexadecimal datatypes
f = 0XFF
print(f)

#Octa decimals datatypes
g= 0O14
print(g)

#Boolean datatypes
f = True
print(type(f))

#Type Conversion
h = int(x)  #float to int
print(type(h))

i = float('22.5') #string to float
print(type(i))

print(bin(11)) # binary conversion
print(hex(11)) # hexadecimal conversion
print(oct(11)) # octadecimal conversion

#Identifiers

userID = 123
userId = 123
user_ID = 123
user_id_ = 123
_userID = 123 #private
__init__ = 123 # special/magic functions