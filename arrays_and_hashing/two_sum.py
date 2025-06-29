# Hash Map (one pass)
# Time complexity: O(n) — each element is visited once
# Space complexity: O(n) — in the worst case, all elements are stored in the hashmap

# class Solution:
#     def twoSum(self, nums: List[int], target:int) -> List[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in seen:
#                 return [seen[diff], i]
#             seen[num] = i

# --------
# Hash Map (two pass)
# Time complexity: O(n) — two separate linear passes over the array
# Space complexity: O(n) — a hashmap stores all elements and their indices

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             seen[num] = i

#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in seen and i != seen[diff]:
#                 return [i, seen[diff]]

# ----------
# Sorting:
# Time complexity: O(nlogn) — due to the sort operation on the array
# Space complexity: O(n) — because a separate list is used to store elements with indices

# class Solution:
#     def twoSum(self, nums: List[int], target:int) -> list[int]:
#         A = []
#         for i, num in enumerate(nums):
#             A.append([num, i])

#         A.sort()
#         i, j = 0, len(nums)-1
#         while i < j:
#             sum = A[i][0] + A[j][0]
#             if sum == target:
#                 return [min(A[i][1], A[j][1]),
#                 max(A[i][1], A[j][1])]
#             elif sum < target:
#                 i += 1
#             else:
#                 j -=1
#         return []

# -----------
# Brute Force
# Time complexity: O(n^2) — checks all pairs in a nested loop
# Space complexity: O(1) — uses only a constant amount of extra space

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
