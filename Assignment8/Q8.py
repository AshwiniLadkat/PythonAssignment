#what happenes internally when python executes an  import module_name  statement?
# When Python executes an import module_name statement, it performs the following steps internally:
# 1. It checks if the module is already loaded in sys.modules. If it is, 
# Python uses the existing module.
# 2. If the module is not already loaded, Python searches for the module in the directories listed in sys.path.
# 3. Once the module is found, Python reads the module's source code and compiles it into bytecode.
# 4. Python then creates a new module object and initializes it by executing the compiled bytecode in the module's namespace.
# 5. Finally, Python adds the module object to sys.modules and makes it available in the current namespace for use. 