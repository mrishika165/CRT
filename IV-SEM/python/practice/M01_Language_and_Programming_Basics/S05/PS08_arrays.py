# arr = np.array([10,20,30])
# print(arr)
# print(np.max(arr))
# print(np.min(arr))
# print(np.sum(arr))
# print("Even numbers list is:",np.arange(2,11,2))
# print("Odd numbers list is:",np.arange(1,10,2))

# third max element in array
# n = int(input())
# ele = list(map(int,input().split()))
# print("Array Ele are:",np.array(ele))
# print("Sum:",np.sum(ele))

# monotonic numbers
nums = list(map(int,input().split()))
inc = True
dec = True 
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        inc = False 
    if nums[i]<nums[i+1]:
        dec = False 
if inc or dec:
    print("Monotonic array")
else:
    print("Not monotonic")


