# A Simple Loop
# The following function finds the maximal element in an array:
import numpy as np
def find_max(arr, size):
    max = 0
    for x in range(size):
        if arr[x] > max:
            max = arr[x]
    return max
arr1 = np.random.randint(1000, size=(1,10))
print(arr1)
val = find_max(arr1[0], len(arr1[0]))
print(val)

# if (max < array[i])
# i++;
# max = array[i]
# Since there are 3 operations in the loop, and the loop is done n times, we add 3n to our already existing 2
# operations to get 3n + 2. So our function takes 3n + 2 operations to find the max (its complexity is 3n + 2). This is
# a polynomial where the fastest growing term is a factor of n, so it is O(n).
