#reversing a list 
# def Reverse_list(li):
#     res = []
#     stop = -1*(len(li)+1)
#     for i in range(-1,stop,-1):
#         res.append(li[i])
#     return res
# li = list(map(int,input().split()))
# print(Reverse_list(li))

#     stop = -1*(len(li)+1)
#     res = [li[i] for i in range(-1,stop,-1)]
#     return res
# li = list(map(int,input().split()))
# print(Reverse_list(li))
#eversing by swapping
# def Reverse_list(li):
#     res = []
#     n = len(li)
#     for i in range(0,n//2):
#         li[i],li[n-1-i] = li[n-i-1],li[i]
#     return li 
# li = list(map(int,input().split()))
# print(Reverse_list(li))

# def Reverse_list(li):
#     res = []
#     for ele in li:
#         res.insert(0,ele)
#     return res 
# li = list(map(int,input().split()))
# print(Reverse_list(li))


# def is_sorted(nums):
#     for i in range(len(nums)-1):
#         if nums[i]>nums[i+1]:
#             return False
#     return True 
# print(is_sorted([1,2,3]))



#count the frequency of elements 
'''
input:[1,2,3,2,4,3,1,5]
output:[1:2,2:2:3:2,4:1,5:1]
'''
# li = [1,2,3,2,4,3,1,5]
# d = {}
# for i in li:
#     if i not in d:
#         d[i]=1 
#     else:
#         d[i] += 1
# print(d)
# print(d.get(2))

li = [1,2,3,2,4,3,1,5]
d = {}
for i in li:
    d[i] = d.get(i,0)+1
print(d)