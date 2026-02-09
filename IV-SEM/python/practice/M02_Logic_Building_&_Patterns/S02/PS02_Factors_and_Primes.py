'''
Read a number from user and  display the count of  number of factors
'''
# n = int(input())
# factor_count = 0 
# for i in range(1,n+1):
#     if n%i == 0:
#         factor_count += 1 
#         print(i,end = " ")
# print(factor_count)


'''
the above code is not optimal whey the input is n there will be no factors from (n//2)+1 to n this reduces time complexity
'''

'''
reversing a integer   cases:- negative numbers and if ends with 0 if u reverse a number it should not start with 0
'''
# n = int(input())
# sign = 1
# rev = 0
# if n< 0:
#     sign = -1
#     n = abs(n)
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10  
# rev = rev * sign 
# print(rev)

'''
other way :- using slicing
'''
# n = int(input())
# if n<0:
#     n = -1*n
#     print(-1 * int(str(n)[::-1]))
# else:
#     print(int(str(n)[::-1]))

'''Leet code (9 Question) Palindrome
Leet code (66 Question) Plus One
Leet code (43 Question) Multiply Strings'''

'''
to check whether number is prime
'''
n = int(input())
count = 0 
for i in range(1,n+1):
    if n % i == 0:
        count+=1 
if count == 2:
    print("Prime")
else:
    print("not prime")

'''Rishika'''
