# Question- What does the id() return? 
    #The id() function in Python returns the memoryaddress ("identity") of an object. 
    #This identity is unique and constant for the object during its lifetime.
# Question - Is the value returned by id() same for two variables holding same value?
    #The value returned by id() may or may not be the same for two variables holding the same value, 
    #depending on the type of the object and how Python manages memory for that type.
    #e.g small int type (range -5 to 256) are cached by python and will have same id() for same value
    #whereas mutable types like lists, dictionaries etc will have different id() even if they hold same value.  