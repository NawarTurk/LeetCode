# ------------
# Two-Pointer 
# Time complexity: O(n) – 
#   • O(n) to iterate through the string using two pointers
#   • Each character is visited at most once by either pointer
#   • Character checks (isalnum and lower) are O(1)
# Space complexity: O(1) – 
#   • Uses only a fixed number of pointers and variables
#   • No extra space proportional to input size

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s)-1
#
#         while l < r:
#             while not s[l].isalnum() and l < r:
#                 l += 1
#             while not s[r].isalnum() and r > l:
#                 r -= 1
#
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1


# ------------
# Reverse-String
# Time complexity: O(n) – 
#   • O(n) to build the cleaned lowercase string (loop, isalnum, lower)
#   • O(n) to reverse the string using slicing
#   • O(n) to compare the original and reversed strings
# Space complexity: O(n) – 
#   • O(n) for the cleaned string
#   • O(n) for the reversed string

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alnum_s = ''.join([c.lower() for c in s if c.isalnum()])
#         return alnum_s == alnum_s[::-1]


# ------------
# Reverse-String with Manual Alphanumeric Check 
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alnum_s = ''.join([c.lower() for c in s if self.is_alpha_numerical(c)])
#         return alnum_s == alnum_s[::-1]
    
#     def is_alpha_numerical(self, c: str) -> bool:
#         return (ord('A') <= ord(c) <= ord('Z') or
#                 ord('a') <= ord(c) <= ord('z') or
#                 ord('0') <= ord(c) <= ord('9'))