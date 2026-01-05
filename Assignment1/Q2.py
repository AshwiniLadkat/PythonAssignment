# Difference between by explaing using id() 
#a=10
#b=10  AND
#a=[10]
#b=[10]

#Defining two integer variables 
a = 10
b = 10
#Displaying the memory addresses of the integer variables
print("Memory address of a (integer):", id(a))      
print("Memory address of b (integer):", id(b))
#Checking if both integer variables point to the same memory location
print("Do a and b (integers) point to the same memory location?", id(a) == id(b))   
print("###############################################################################")  

#Defining two list variables 
a = [10]    
b = [10]
#Displaying the memory addresses of the list variables
print("Memory address of a (list):", id(a))
print("Memory address of b (list):", id(b))    
#Checking if both list variables point to the same memory location
print("Do a and b (lists) point to the same memory location?", id(a) == id(b))  
print("###############################################################################")

#explanation :  
    #"Integer variables with the same value points to the same memory location due to integer caching in Python. 
    #In Python, a specific range of small integers is pre-allocated and cached in memory for optimization purposes. This range is from -5 to 256.
    
    #However, list variables, being mutable objects,due to having  dynamic resizing capability  are stored at different memory locations even if they contain the same elements."    
