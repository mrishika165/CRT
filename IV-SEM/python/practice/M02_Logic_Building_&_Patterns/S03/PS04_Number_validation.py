'''
check whether number is armstrong or not
'''
# n = int(input())
# r = len(str(n))
# original = n
# total = 0
# while n > 0:
#     digit = n % 10 
#     total += (digit)**r 
#     n = n//10 
# if(total == original ):
#     print("Armstrong")
# else:
#     print("No")

''' 
other way to check whether the number is armstrong or not
'''
# n = int(input())
# r = len(str(n))
# total = 0
# for i in str(n):
#     total += int(i) ** r
# if n == total:
#     print("Armstrong")
# else:
#     print("No")

'''
check whether the number is Perfect number or not
n = 6
factors of 6:1,2,3,6
except the number itself if u add the factors it should is called perfect number
'''
# n = int(input())
# total = 0
# for i in range(1,n//2+1):
#     if (n%i==0):
#         total+=i 
# if total == n:
#     print("Perfect")
# else:
#     print("No")

'''
check whether the number is strong or not
a number is strong if the sum of the factorials of the digit is equal to the given number
'''
# n = int(input())
# original = n
# total = 0 
# while n > 0:
#     digit = n%10 
#     fact = 1
#     for i in range(1,digit+1):
#         fact *= i 
#     total += fact
#     n = n//10 

# if total == original:
#     print("Strong")
# else:
#     print("No")

