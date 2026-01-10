#Write program to display:

 #.Data Type
 #.Memory Address
 #.Size in bytes of a variable entered from user
 
# Program to display Data Type, Memory Address, and Size in bytes of a variable entered from user       
# Accepting input from the user
user_input = input("Enter a value: ")       
# Displaying the value entered by the user
print("Value entered by the user:", user_input)
# Displaying the Data Type of the variable
print("Data Type of the variable:", type(user_input))
# Displaying the Memory Address of the variable
print("Memory Address of the variable:", id(user_input))
# Displaying the Size in bytes of the variable
import sys  
print("Size in bytes of the variable:", sys.getsizeof(user_input))


    