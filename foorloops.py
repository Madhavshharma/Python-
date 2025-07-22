# numbers='89,23,56;775.456:'
# numbers=input("Enter a string of numbers with separators:-- ")

# seprators=" "
# for i in numbers:
#     if not i.isnumeric():
#         seprators=seprators+i
# print("seprators are:", seprators)

# # Exploring the use of separators in a string of numbers
# # This code snippet demonstrates how to extract separators from a string of numbers



quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
 
# Use a for loop and an if statement to print just the capitals in the quote above.
uppercase=" "
capital_letters = [char for char in quote if char.isupper()]

# Print them separated by spaces
print(''.join(capital_letters))