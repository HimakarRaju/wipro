import unittest

//what to do to tun tests ?


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
        self.assertEqual(DataStructureOperations.update_tuple(
            my_tuple, 1, 10), (1, 10, 3, 4, 5))

        # Slice tuple
        self.assertEqual(DataStructureOperations.slice_tuple(
            my_tuple, 1, 4), (2, 3, 4))

    def test_dict_operations(self):
        my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

        # Access dict
        self.assertEqual(DataStructureOperations.access_dict(my_dict, 'c'), 3)

        # Update dict
        self.assertEqual(DataStructureOperations.update_dict(my_dict, 'b', 10),
                         {'a': 1, 'b': 10, 'c': 3, 'd': 4, 'e': 5})

        # Slice dict keys
        self.assertEqual(DataStructureOperations.slice_dict_keys(
            my_dict, 'b', 'd'), {'b': 10, 'c': 3, 'd': 4})

    def test_set_operations(self):
        my_set = {1, 2, 3, 4, 5}

        # Access set
        self.assertTrue(DataStructureOperations.access_set(my_set, 3))

        # Add to set
        self.assertEqual(DataStructureOperations.add_to_set(
            my_set, 6), {1, 2, 3, 4, 5, 6})

        # Slice set
        self.assertEqual(DataStructureOperations.slice_set(
            my_set, 2, 4), {2, 3, 4})
