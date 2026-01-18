#Explain the steps to craete and use user defined module?
# Steps to create and use a user-defined module in Python:
# 1. Create a Python file (module) with a .py extension. For example, create a file named mymodule.py.
# 2. Define functions, classes, or variables in this file that you want to include in your module.
# 3. Save the file in a directory where Python can find it (the same directory as your main program or in a directory listed in sys.path).
# 4. In your main program, use the import statement to include the module. For example, use import mymodule.
# 5. Call the functions or access the variables defined in the module using the module name as a prefix. For example, mymodule.myfunction().    
# Example:
# mymodule.py   
def greet(name):
    return f"Hello, {name}!"
# main.py
import mymodule
def main():
    name = input("Enter your name: ")
    message = mymodule.greet(name)
    print(message)
    
if __name__ == "__main__":
    main()