"""
Arrays

Implementation from first principles.

This file accompanies the README.md explanation.

"""

# Simple explanation

numbers = [10,20,30.40]

print (numbers[0])
print (numbers[2])

"""
Demonstrating operations
Using the numbers array
"""
# 1. Accessing is O(1)
print(numbers[1])

# 2. Updating takes O(1) complex time
numbers[1] = 50

# 3. Append
numbers.append(60)

# 4. Inserting in the middle shifts later elements, hence O(n)
numbers.insert(1, 15)


# 5. Deleting is O(n)
numbers.pop()
print(numbers)

"""
The following code demonstrates linear search and binary search of arrays by hand-rolling
Python already has built-in methods for this
"""

#Function for linear search

def linear_search(arr, target):
  """ O(n): checks each element until found"""
  for i, value in enumerate(arr):
    if value == target:
      return i
  return -1

# Function for binary search
def binary_search(arr, target):
  """ O(log n): array must be sorted. Repeatedly halves the search space."""
  low, high = 0, len(arr)-1
  while low <=high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid -1
  return -1

# Usage examples
nums = [40,10,30,20,50]
print(linear_search(nums,30))

sorted_nums = sorted(nums)
print(binary_search(sorted_nums, 30))

"""Built-in ways for searching an array"""

# using nums array

#Linear search equivalent
nums.index(30) # returns 2, raises ValueError if not found. Also an O(n) operation under the hood
30 in nums     # returns True/False O(n) under the hood

#Binary search equivalent - bisect module
import bisect
sorted_nums = sorted(nums)
i = bisect.bisect_left(sorted_nums, 30)
found = i < len(sorted_nums) and sorted_nums[i] == 30 # True

