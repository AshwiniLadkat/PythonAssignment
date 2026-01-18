#What happenes if module contains print statements outside any function?
# When a module contains print statements outside any function, those print statements are executed immediately when the module is imported.
# This means that as soon as the module is imported, the print statements will run and display
# their output to the console.
# This behavior can be useful for debugging or providing information when the module is loaded,
# but it can also lead to unwanted output if the module is imported in other scripts.
# Example:
print("This print statement is outside any function and will execute upon import.")
def example_function():
    print("This is a function inside the module.")
# When this module is imported, the first print statement will execute immediately,
# while the print statement inside example_function will only execute when the function is called.