# Write a Python program that takes a string input from the user and checks if it is a palindrome.
# A palindrome is a string that reads the same backward as forward

# Program to check if a string is a palindrome

# # Method1
# string = input("Enter a string\n")          # Get user input
# if string == string[::-1]:                  # Check if the string is a palindrome
#     print("The string is a palindrome\n")
# else:
#     print("The string is not a palindrome\n")


# Method2
String = input("Enter a string\n")
inverse_string = reversed(String)
if list(String) == list(inverse_string):
    print("The string is a palindrome\n")
else:
    print("The string is not a palindrome\n")
