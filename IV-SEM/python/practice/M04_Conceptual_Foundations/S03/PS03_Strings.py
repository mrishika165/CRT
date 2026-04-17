'''
String is immutable 
'''
# s = "nandu"
# s = s.capitalize()
# print(s)

'''
reversing a string
'''
# def reverse(s):
#     res = ""
#     for i in s:
#         res = i + res
#     return res
# s = input()
# print(reverse(s))

# def Reverse_str1(s):
#     res = ""
#     stop = -1*(len(s)+1)
#     for ch in range(-1,stop,-1):
#         res = res+s[ch]
#     return res
# s = input()
# print(Reverse_str1(s))

# def is_palindrome(s):
#     res = ""
#     for i in s:
#         res = i + res 
     
#     if res == s:
#         return(True)
#     else:
#         return(False)
# s = input()
# print(is_palindrome(s))

# s = "madam"
# print(s[:-1])

'''
checking for anagrams
'''
# def Frequency_count(s):
#     d = {}
#     for ch in s:
#         if ch not in d:
#             d[ch] = 1 
#         else:
#             d[ch]+=1
#     return d
# s = input()
# print(Frequency_count(s))


# def anagram(s1,s2):
#     return Frequency_count(s1) == Frequency_count(s2)
# s1= input()
# s2 = input()
# print(anagram(s1,s2))

from collections import Counter
print(Counter("aabbcc"))