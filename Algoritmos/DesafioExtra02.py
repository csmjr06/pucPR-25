"""
In this exercise, you will create your own versions of Python’s list functions without using built-in methods like .append(), .sort(), or .pop(). Instead, you will write your own logic using loops and conditionals.
"""

# 1. Implement a function Append ( append(lst, value) ) that adds a value to the end of a list. Example: append([1,2],3) -> [1, 2, 3]
def append(lst, value):
    """
    Appends a value to the end of a list.
    """
    for i in range(len(lst), len(lst) + 1):
        lst += [value]
        return lst
# Test the function
print(append([1, 2], 3))  # Output: [1, 2, 3]

# 2. Implement a function Insert ( insert(lst, index, value) ) that inserts a value at a specific index in a list. Example: insert([1,3], 1, 2) -> [1, 2, 3]
def insert(lst, index, value):
    """
    Inserts a value at a specific index in a list.
    """
    if index < 0 or index > len(lst):
        raise IndexError("Index out of range")
    new_lst = []
    for i in range(len(lst)):
        if i == index:
            new_lst += [value]
        new_lst += [lst[i]]
    if index == len(lst):  # Handle case where index is at the end
        new_lst += [value]
    return new_lst

# Test the function
print(insert([1, 3], 1, 2))  # Output: [1, 2, 3]

# 3.Removes the first occurrence of value from the list. Example: remove([1, 2, 3, 2], 2) → [1, 3, 2]
def remove(lst, value):
    """
    Removes the first occurrence of value from the list.
    """
    new_lst = []
    found = False
    for i in range(len(lst)):
        if lst[i] == value and not found:
            found = True
        else:
            new_lst += [lst[i]]
    return new_lst  

# Test the function
print(remove([1, 2, 3, 2], 2))  # Output: [1, 3, 2]

#4. Pop Function (pop(lst, index=None))
def pop(lst, index=None):
    """
    Removes and returns the last value, or at the specified index from the list, if provided.
    """
    if index is None:
        index = len(lst) - 1
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of range")
    value = lst[index]
    new_lst = []
    for i in range(len(lst)):
        if i != index:
            new_lst += [lst[i]]
    return value, new_lst
# Test the function
print(pop([1, 2, 3, 4]))  # Output: (4, [1, 2, 3])
    
#5. Returns the position of the first occurrence of value.
def index(lst, value):
    """
    Returns the index of the first occurrence of value in the list.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1  # Return -1 if value is not found
# Test the function
print(index([10, 20, 30, 40], 20))  # Output: 1

# 6. Returns how many times value appears in the list.
def count(lst, value):
    """
    Returns the number of occurrences of value in the list.
    """
    count = 0
    for i in range(len(lst)):
        if lst[i] == value:
            count += 1
    return count
# Test the function
print(count([1, 2, 3, 2, 4], 2))  # Output: 2

# 7. everses the list order in place.
def reverse(lst):
    """
    Reverses the list in place.
    """
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst += [lst[i]]
    return new_lst
# Test the function
print(reverse([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]

# 8. Sorts the list in ascending order manually.
def sort(lst):
    """
    Sorts the list in ascending order.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
# Test the function
print(sort([3, 1, 4, 2]))  # Output: [1, 2, 3, 4]

# 9. Adds all elements from another list (iterable) to the current list.
def extend(lst1, iterable):
    """
    Extends the list with elements from an iterable.
    """
    for item in iterable:
        lst1 += [item]
    return lst1
# Test the function
print(extend([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

# 10. 
def clear(lst):
    """
    Clears the list.
    """
    for i in range(len(lst)):
        lst[:] = []

# Test the function 
print(clear([1, 2, 3]))  # Output: []