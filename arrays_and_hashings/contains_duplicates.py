# Hash set length
# Time complexity: O(n) – set() conversion scans all elements once
# Space complexity: O(n) – set stores up to n unique elements

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) > len(set(nums))


# ------------
# Hash Set
# Time complexity: O(n) – each lookup and insert is O(1) on average
# Space complexity: O(n) – set stores seen elements

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False


# ------------
# Sorting
# Time complexity: O(nlogn) – due to in-place sorting
# Space complexity: O(1) – assuming sorting is in-place (Timsort)

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False


# ------------
# Brute Force
# Time complexity: O(n^2) – checks every pair
# Space complexity: O(1) – uses no extra space

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
