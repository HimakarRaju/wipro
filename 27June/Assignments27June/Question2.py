"""
Write a program that asks the user for their first and last name, and then prints them in reverse order with a space between them.

**Example:**
```
Input: John Doe
Output: eoD nhoJ
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name[::-1] + " " + first_name[::-1])
