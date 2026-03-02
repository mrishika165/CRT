# def liner_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i 
#     return -1 
# print(linear_search())



'''
binary search
'''
arr= list(map(int,input().split()))
target = int(input())
n = len(arr)
low = 0 
high = len(arr)-1 
mid = (low+high)//2
