#What are the differnent way to import module ? which one recommanded and why?
# There are several ways to import modules in Python:
# 1. import module_name: This imports the entire module and requires you to use the
#    module name as a prefix to access its functions and variables.
# 2. from module_name import function_name: This imports a specific function or variable
#    from the module, allowing you to use it directly without the module name prefix.
# 3. from module_name import *: This imports all functions and variables from the module
#    into the current namespace, allowing you to use them directly.
# 4. import module_name as alias: This imports the module and assigns it an alias,
#    allowing you to use the alias as a prefix to access its functions and variables.       
# The recommended way to import modules is to use the first method (import module_name)
# or the fourth method (import module_name as alias). This is because it keeps the
# namespace clean and makes the code more readable.