'''
Arithmetic + - * / % // **
Assignment = += -=.....
Relational < > <= == ----->Boolean return type
Logical and or not   ----->Boolean return type
Bitwise & | ~ ^ << >>
Membership in ,not in ------>Boolean return type
Identity is,is not     ------>Boolean return type
among these Unary operators are ~,not remaining all are binary

'''
#Bitwise operators
x = 7#00000111
y = 13
print(x&y) # both 1 only then 1 
print(x | y)# same numbers 0 when bits different 1
print(~x)#add 1 and multiply by -1
print(x<<2)  #removes left 2 bits and adds zeros to right  left shift
print(x>>2)   #removes right 2 bits and adds zeros to left
#Membership
print(100 in [12,45,78])  #return type is boolean
print("on" in "python")
#Identity operators
x = 10
y = 20
z = 10
print(x is y) 
print(x is z)
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)   # output is false as integers are immutable where as lists are mutable

