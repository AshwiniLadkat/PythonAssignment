#Explain why the strings are immutablein python?what happened internally when you modify a string variable?
# Strings are immutable in Python because once a string object is created, 
# its value cannot be changed.
# When you modify a string  
original_string = "Hello, Ashwini!"
modified_string = original_string.replace("World", "Python")
print("Original String:", original_string)  # Output: Hello, World!
print("Modified String:", modified_string)  # Output: Hello, Python!
# Explanation:
    #When you attempt to modify a string, Python does not change the original string.
    # Instead, it creates a new string object with the modified value. 
    
    