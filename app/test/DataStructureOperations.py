class DataStructureOperations:
    # Access an element in a list by index
    @staticmethod
    def access_list(my_list, index):
        accessed_val = my_list[index]
        return accessed_val

    # Update an element in a list by index
    @staticmethod
    def update_list(my_list, index, value):
        my_list[index] = value
        return my_list

    # Slice a list from start index to end index
    @staticmethod
    def slice_list(my_list, start, end):
        sliced_list = my_list[start:end]
        return sliced_list

    # Access an element in a tuple by index
    @staticmethod
    def access_tuple(my_tuple, index):
        return my_tuple[index]

    # Update an element in a tuple by index
    @staticmethod
    def update_tuple(my_tuple, index, value):
        updated_tup = my_tuple[:index] + (value,) + my_tuple[index + 1:]
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
        my_dict[key] = value
        return my_dict

    # Slice dictionary keys from start_key to end_key
    @staticmethod
    def slice_dict_keys(my_dict, start_key, end_key):
        keys = list(my_dict.keys())
        sliced_keys = keys[start_key:end_key]
        return {key: my_dict[key] for key in sliced_keys}

    # Check if an element is in a set
    @staticmethod
    def access_set(my_set, element):
        return element in my_set

    # Add an element to a set
    @staticmethod
    def add_to_set(my_set, element):
        my_set.add(element)
        return my_set

    # Slice a set from start index to end index
    @staticmethod
    def slice_set(my_set, start, end):
        sorted_list = sorted(my_set)
        sliced_set = sorted_list[start:end]
        return set(sliced_set)
