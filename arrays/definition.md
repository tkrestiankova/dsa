# Arrays
- **linear** data type
- **indexed** - each element in the array has an index, a number that says where in the array the element is located
- we can imagine an array as a large chunk of memory divided into smaller blocks of memory and each block is capable of storing a data value of sosme type
- values are of the **same data type**
- **fixed size** - after an array is initialized/constructed, it cannot be changed (static memory allocation)

## Algorithm: Find The Lowest Value in an Array

1. Go through the values in the array one by one.
2. Check if the current value is the lowest so far, and if it is, store it.
3. After looking at all the values, the stored value will be the lowest of all values in the array.

```python
my_list = [8768, 876, 987, 89237, 7234, 87, 872364, 73462, 67, 7634, 9890]
lowest_value = my_list[0]

for value in my_list:
  if value < lowest_value:
    lowest_value = value

print(f"Lowest value in {my_list} is {lowest_value}")
```

## Time complexity
- the number of operations needed to run an algorithm on large amounts of data
- in the example above (find the lowest value in an array), each value from the array are compared one time. Every such comparison can be considered as operation and each operation take some time. This means that the total time this algorithm needs to find the lowest value depends on the number of values in the array - the time it takes to find the lowest value is therefore linear with the number of values
- *O(n)* - the algorithm must do *n* operations in an array with *n* values to find the lowest value, because the algorithm must compare each value one time
