
'''
n = 4
output:
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
'''
n = int(input())
for i in range(1,n+1):
    print("*"*i + " "*(2(n-i))+"*"*i)
for j in range(1,n+1):
    print("*"*(n+1-i) + " "*()+"*"*(n+1-i))