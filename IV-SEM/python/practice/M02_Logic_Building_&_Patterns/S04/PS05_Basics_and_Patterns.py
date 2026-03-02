'''
input:4
output:
* * * * 
* * * * 
* * * * 
* * * * 
'''

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*",end = " ")
#     print()

'''
n = 4 
*
* *
* * *
* * * *
'''

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end = " ")
#     print()


'''
n = 4
output:
* * * *
* * * 
* * 
*
'''
# n  = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*",end = " ")
#     print()

# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end = " ")
#     print()

'''
n = 4 
output:
1
2 3
4 5 6
7 8 9 10
'''
# n = int(input())
# k = 1
# for i in range(1,n+1):
#     for j in range(i):
#         print(k,end = " ")
#         k += 1
#     print()

'''
n = 4
output:
A
A B
A B C
A B C D
'''
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end = " ")
#     print()

''' 
n = 4
output:
A
B C
D E F
G H I J
'''
# n = int(input())
# k = 65
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(k),end = " ")
#         k += 1
#     print()

'''
hallow square
n = 4
* * * *
*     *
*     *
* * * *
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()