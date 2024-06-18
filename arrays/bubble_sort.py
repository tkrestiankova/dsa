"""
Algorithm: Bubble sort
Time complexity: O(n^2)

1. Go through the array, one value at a time
2. For each value, compare the value with the next value
3. If the value is higher than the next one, swap the values so that the highest value comes last
4. Go through the array as many times as there are values in the array
"""

my_list = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_list)

# we need to go through this list as many times
# as there are items in the array
for i in range(n):
  # we iterate through the array
  # n-i-1 because last elements are already sorted
  # we do not need to compare them again
  for j in range (0, n-i-1):
    # if the value is higher than the next one, swap them
    if my_list[j] > my_list[j+1]:
      my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(f"My list after sorting: {my_list}")
