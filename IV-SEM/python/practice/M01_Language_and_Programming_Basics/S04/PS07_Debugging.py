#Debugging in errors
'''
bug means errors 
Debugging-->Finding and fixing errors 
Types of errors:
1.Syntax error-missing of colon,missing of identation
2.Runtym error-division by zero
3.logical error-wrong approach,formulae

pdb commands:
1.n---->to execute output in new line
2.p variable ---->to get the value of a variable
3.I--->list nearby code
4.c--->continue execution
5.s---->to start the function
6.r--->to return from the function
7.h --->help
8.q --->Quit the execution
'''
# try:
#     a = int(input("Enter a number:"))
#     print(10/a)
# except ZeroDivisionError:
#     print("cannot devide by zero")
# except ValueError:
#     print("INVALID error")



import pdb 
def add(a,b):
    pdb.set_trace() #set the breakpoint 
    return a+b 
a = int(input("Enter first number:"))
b = int(input("Enter the second number:"))
print(add(a,b))