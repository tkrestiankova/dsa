"""
Algorithm: Selection sort

Basic version
1. Go through the array to find the lowest value
2. Move the lowest value to the front of the unsorted part of the array
3. Go through the array again as many times as there are values in the array

Improved version
Note: In the basic version, we use operations like .pop() and .insert()
which are responsible for shifting values in the list. This is a very
time consuming operation! Instead of .pop() and .insert(), we can swap
values instead.


Time complexity: O(n^2)
- 

Source: https://www.w3schools.com/dsa/dsa_algo_selectionsort.php
"""

# 1. BASIC VERSION

my_list = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_list)

# we need to go through this list as many times
# as there are items in the array
for i in range(n-1):

    # we go through the list to find the lowest value
    for j in range(i+1, n):
        if my_list[j] < my_list[i]:
            lowest_value = my_list[j]
            # we need to remember the index of the lowest value
            lowest_value_index = j

    # Here we are shifting values in the list
    # to move the lowest value to the front of 
    # the unsorted part of the array
    lowest_value = my_list.pop(lowest_value_index)
    my_list.insert(i, lowest_value)
    print(f"My list after iteration: {my_list}")

# 1. OPTIMIZED VERSION

my_list = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_list)

# we need to go through this list as many times
# as there are items in the array
for i in range(n-1):

    # we go through the list to find the lowest value
    for j in range(i+1, n):
        if my_list[j] < my_list[i]:
            # we need to remember the index of the lowest value
            lowest_value_index = j

    # Perform shift
    my_list[i], my_list[lowest_value_index] = my_list[lowest_value_index], my_list[i]
    print(f"My list after iteration: {my_list}")
    
    
    
  
