'''
Fibonacci series
'''
# def fibo(n):
#     if n <0:
#         return "Invalid"
#     elif n ==0:
#         return 0 
#     elif n ==1:
#         return 1
#     return fibo(n-1)+fibo(n-2)
# n = int(input())
# print(fibo(n))
    
'''
GCD of 2 numbers
'''
# def GCD(a,b):
#     while b!=0:
#         a,b = b , a%b 
#     return a 
# a = int(input())
# b = int(input())
# print(GCD(a,b))

def GCD(a,b):
    if b==0:
        return a 
    return GCD(b,a%b)
print(GCD(1,10))
