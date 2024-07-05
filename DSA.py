"""
Question: Python Data Structure
Operations
Task
1. Write the code to pass all tests.
2. Follow the instructions below in order to successfully complete this task.

Task Details
In this assessment, you'll be working with different Python data structures: lists, tuples, dictionaries, and sets.
Your task is to perform various operations on these data structures, including accessing, updating, and slicing.
Task: Write Python code to perform the following operations on each of the data structures:
lists, tuples, dictionaries, and sets.
1. Accessing: Access a specific element or value from each data structure.
2. Updating: Update a value or element in each data structure.
3. Slicing: Slice each data structure to retrieve specific portions of it.
Instructions:
1. Write Python code snippets for each operation described above for lists, tuples, dictionaries, and sets.
2. Include comments to explain each operation.
3. Ensure that your code is concise,
Here are the input and output details for each task:
Input:
* For each data structure (list, tuple, dictionary, set), you'll have an initial instance of that data structure.
* Any required parameters to perform the operations (e.g., index for accessing, key-value pairs for dictionaries,
slice indices for slicing).

Output:
1. Accessing:
* The specific element or value accessed from each data structure.
2. Updating:
Index
* The updated data structure after modifying a value or element.
3. Slicing:
* The sliced portion of each data structure as specified.
Example:
List:
Input:
* Initial list: [1, 2, 3, 4, 5]
* Index: 2 Output:
* Accessed value: 3
"""


def access_list(my_list, index):
    accessed_val = my_list[index]
    return accessed_val


def update_list(mylist, index, value):
    mylist[index] = value
    return mylist


def slice_list(my_list, start, end):
    sliced_list = my_list[start:end]
    return sliced_list


def access_tuple(my_tuple, index):
    accessed_val = my_tuple[index]
    return accessed_val


def update_tuple(my_tuple, index, value):
    pass


def slice_tuple(my_tuple, start, end):
    sliced_tuple = my_tuple[start:end]
    return sliced_tuple


def access_dict(my_dict, key):
    accessed_value = my_dict[key]
    return accessed_value


def update_dict(my_dict, key, value):
    my_dict[key] = value
    return my_dict


def slice_dict_keys(my_dict, start_key, end_key):
    sliced_dict = my_dict[start_key:end_key]
    return sliced_dict


def access_set(my_set, element):
    return [True if element in my_set else False]


def add_to_set(my_set, element):
    my_set.add(element)
    return my_set


def slice_set(my_set, start, end):
    pass
