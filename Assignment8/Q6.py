#Why is from module import * discouraged in professionla code ?
# Using from module import * is discouraged in professional code for several reasons:
# 1. Namespace Pollution: It imports all the names from the module into the current namespace
#    which can lead to name conflicts and make it difficult to determine where a particular
#    name came from.
# 2. Readability: It reduces code readability as it becomes unclear which names are being
#    used from the module, making it harder for others (or yourself) to understand the code.
# 3. Maintainability: It can lead to maintenance issues as changes in the imported module
#    can inadvertently affect the current code if there are name conflicts.
# 4. Debugging Difficulty: It makes debugging more challenging since it is not clear
#    which module a particular name belongs to.
# Instead, it is recommended to use explicit imports (import module_name) or
# selective imports (from module_name import specific_name) to maintain clarity

