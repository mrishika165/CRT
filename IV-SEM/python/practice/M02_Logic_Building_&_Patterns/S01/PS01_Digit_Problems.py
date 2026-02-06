'''
write a python code to count the digits of number.
'''
# n = int(input())
# count = 0
# while n > 0:
#     count+=1 
#     n = n//10 
#     print(count)

''' 
sum of digits of a number
'''
# n = int(input()) 
# sum = 0 
# while n>0:
#     sum += n%10 
#     n = n//10 
# print(sum)

'''
Reversing the number
'''
# num = int(input())
# rev = 0
# while num> 0:
#     rev = rev*10 +num%10 
#     num = num//10 
# print(rev)
'''
count the even and odd digits
'''
# n = int(input())
# even = 0 
# odd = 0 
# while n > 0:
#     digit = n%10 
#     if digit%2 == 0:
#         even +=1 
#     else:
#         odd+= 1 
#     n = n//10
# print(even)
# print(odd)
'''
largest digit of a anumber
'''
n = int(input())
largest =0 
while n > 0 :
    digit = n%10 
    if digit>largest:
        largest = digit 
    n = n//10 
print(largest)