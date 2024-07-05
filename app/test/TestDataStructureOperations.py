from app.data_structure_operations import DataStructureOperations
import unittest


class TestDataStructureOperations(unittest.TestCase):
    def test_list_operations(self):
        my_list = [1, 2, 3, 4, 5]

        # Access list
        self.assertEqual(DataStructureOperations.access_list(my_list, 2), 3)

        # Update list
        self.assertEqual(DataStructureOperations.update_list(
            my_list, 1, 10), [1, 10, 3, 4, 5])

        # Slice list
        self.assertEqual(DataStructureOperations.slice_list(
            my_list, 1, 4), [10, 3, 4])

    def test_tuple_operations(self):
        my_tuple = (1, 2, 3, 4, 5)

        # Access tuple
        self.assertEqual(DataStructureOperations.access_tuple(my_tuple, 2), 3)

        # Update tuple
       …
[11:33 pm, 04/07/2024] HimakarRaju: class DataStructureOperations:
    # Access an element in a list by index
    @staticmethod
    def access_list(my_list, index):
        accessed_val = my_list[index]
        return accessed_val

    # Update an element in a list by index
    @staticmethod
    def update_list(my_list, index, value):
        mylist[index] = value
        return mylist

    # Slice a list from start index to end index
    @staticmethod
    def slice_list(my_list, start, end):
        sliced_list = my_list(start:end)
        return sliced_list

    # Access an element in a tuple by index
    @staticmethod
    def access_tuple(my_tuple, index):
        return my_tuple[index]
        

    # Update an element in a tuple by index
    @staticmethod
    def update_tuple(my_tuple, index, value):
        updated_tup = my_tuple[:index-1]+(value)+(my_tuple[index+1:])
        return updated_tup

    # Slice a tuple from start index to end index
    @staticmethod
    def slice_tuple(my_tuple, start, end):
        return my_tuple[start:end]

    # Access a value in a dictionary by key
    @staticmethod
    def access_dict(my_dict, key):
        return my_dict[key]

    # Update a value in a dictionary by key
    @staticmethod
    def update_dict(my_dict, key, value):
        my_dict[key]=value
        return my_dict

    # Slice dictionary keys from start_key to end_key
    @staticmethod
    def slice_dict_keys(my_dict, start_key, end_key):
        return my_dict[start_key:end_key]

    # Check if an element is in a set
    @staticmethod
    def access_set(my_set, element):
        return [True if element in my_set else False]

    # Add an element to a set
    @staticmethod
    def add_to_set(my_set, element):
        my_set.add(element)
        return my_set

    # Slice a set from start index to end index
    @staticmethod
    def slice_set(my_set, start, end):
        sliced_set = my_set[start:end]
        return sliced_set