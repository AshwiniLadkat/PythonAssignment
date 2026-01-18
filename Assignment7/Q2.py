#Why should excessive use of global variables be avoided in large programs? 
#ANS-
#Excessive use of global variables should be avoided in large programs for several reasons:
#1. Namespace Pollution: Global variables occupy the global namespace, which can lead to
#   naming conflicts and make it difficult to track variable usage.
#2. Reduced Readability: When many global variables are used, it becomes harder to understand
#3.Difficult to Trace and Debug: A global variable can be modified by any function or 
#   part of the program. When a bug occurs with an unexpected value,
#   tracking down which section of the code changed the variable's state becomes a difficult and time-consuming process.
# Creates Tight Coupling: Functions and modules that rely on global variables are implicitly coupled, 
#   or linked together. This tight coupling reduces modularity; 
#   changing a global variable's use in one function can unintentionally break other, 
#   seemingly unrelated, parts of the program.
# Reduces Modularity and Reusability: Code that depends on specific global states cannot be easily
#   reused in other contexts or projects without dragging along all its environmental dependencies. 
#   Writing code to be more self-contained (e.g., passing data as parameters 
#   or using object attributes) increases its portability.
# Leads to Naming Conflicts (Namespace Pollution): In a large codebase with multiple developers or
#   integrated third-party libraries, using common global variable names can lead to naming collisions where one variable overwrites another, causing unexpected behavior.
# Causes Concurrency and Threading Issues: In multi-threaded applications, 
#   shared global variables introduce the risk of data races and race conditions, where multiple threads try to read and write to the variable simultaneously. To prevent this, complex synchronization mechanisms (like locks or mutexes) are required, which adds complexity and can introduce performance bottlenecks or deadlocks.
# Makes Unit Testing Difficult: Code that accesses global state is hard to unit test in isolation
#   because the test environment must be able to set up and reset the global state for each test case. This makes tests brittle and complex, as the order of tests might matter if the state is not properly reset.
#   Violates Information Hiding: Using global variables breaks the software design principle of information hiding (encapsulation) by making internal data accessible everywhere, rather than through controlled interfaces (APIs). 