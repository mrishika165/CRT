# patterns using only 1 loop
'''
li = [1,2,3,4,5]
output:[1,4,9,16,25]
'''
# li = list(map(int,input().split()))
# result  = []
# for i in li:
#     result.append(i**2)
# print(result)
 
'''
using comprehensiion
'''
# li = list(map(int,input().split()))
# ans = [i**2 for i in li]
# print(ans)

'''
print only even
'''
# li = list(map(int,input().split()))
# res = []
# for i in li:
#     if i%2==0:
#         res.append(i)
# print(res)

'''
using comprehension
'''
# li = list(map(int,input().split()))
# ans = [i for i in li if i%2==0]
# print(ans)

'''
Join method
li = ['a' ,'b' , 'c']
output:'a b c'
'''
# li = ['a' ,'b' , 'c']
# res = ""
# for ch in li:
#     res= res+ch+" "
# print(res)

# li = ['a' ,'b' , 'c']
# print(" ".join(li))

'''
pyramid:
n = 4
output:
   *
  * *
 * * *
* * * *
'''
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i) +"* "*i)

'''
inverted pyramid
n = 4
* * * *
 * * *
  * * 
   *
'''
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(i-1)+"* "*(n+1-i))

'''
diamond 
n = 4
output:
   *
  * *
 * * *
* * * *
 * * *
  * * 
   *
'''
# n = int(input())
# for i in range(1,n):
#    print(" "*(n-i)+"* "*i)
# for i in range(1,n+1):
#    print(" "*(i-1)+"* "*(n+1-i))

'''
n = 4
output:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
'''



'''
n = 4
   1
  1 2
 1 2 3
1 2 3 4
'''
# n = int(input())
# for i in range(1,n+1):
#    for j in range(n-i):
#       print(" ",end = "")
#    for k in range(1,i+1):
#       print(k,end =" ")
#    print()


# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+" ".join([str(k) for k in range(1,i+1)]))

'''
n = 4
   1
  2 2
 3 3 3
4 4 4 4
'''
n = int(input())
for i in range(1,n+1):
   print(" "*(n-i),end = " ")
   for j in range(1,i+1):
      print(i,end = " ")
   print()

   