# ------------
# Sorting
# Time complexity: O(n log n) – 
#   • O(n log n) to sort string s using Timsort
#   • O(n log n) to sort string t using Timsort
#   • O(n) to compare the two sorted lists
#   • Overall dominated by the sorting operations
# Space complexity: O(n) – 
#   • O(n) space to store the sorted version of s
#   • O(n) space to store the sorted version of t
#   • Strings are immutable, so sorted() must create new lists

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return sorted(s) == sorted(t)



# ------------
# Hash Map Character Counting
# Time complexity: O(n)
#   • O(n) to iterate over both strings of length n
#   • Hash map insertions and lookups are O(1) on average per character
#   • Final comparison of two dictionaries is O(1) since there are at most 26 keys
# Space complexity: O(1)
#   • At most 26 entries per dictionary for lowercase English letters
#   • Space does not scale with input size beyond the fixed alphabet

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         countS, countT = {}, {}
#
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#  
#         return countS == countT