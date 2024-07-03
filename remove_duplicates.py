def remove_duplicates(nums):

    # Sort the input list
    nums = sorted(nums)

    # Initialize a new list to store the unique elements
    unique_nums = []

    # Iterate through the sorted list and add unique elements to the new list
    for num in nums:
        if len(unique_nums) == 0 or num != unique_nums[-1]:
            unique_nums.append(num)

    # Fill the remaining positions with underscores
    while len(unique_nums) < len(nums):
        unique_nums.append("_")

    return unique_nums


print(remove_duplicates(nums=[1, 1, 2]))  # Output: [1, 2, '_']
