#How does python insternally indentify teh start and end of a code block  using indentation?
# Python uses indentation to identify the start and end of a code block.
# A code block is defined by its indentation level, which is determined by the number of spaces
# or tabs at the beginning of a line. When a line of code is indented, it indicates that it is
# part of a code block that is nested within the previous line. 
# The end of a code block is identified by a decrease in indentation level. 
# Consistent indentation is crucial
# for Python to correctly interpret the structure and flow of the code.
# Example:
def example_function():
    print("This is the start of the code block")
    if True:
        print("This is a nested code block")
    print("This is the end of the code block")
