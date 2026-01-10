#What are the bytes in python? Why they are imutable?
    #Bytes are immutable sequences of single bytes ranging from 0 to 255.
    #They are used to represent binary data and text encoded in specific encodings.
    #Bytes are immutable because once a bytes object is created, its content cannot be changed.
    #When you attempt to modify a bytes object, Python raises a TypeError.
# Example:
b = bytes([65, 66, 67]) # Creating a bytes object
print("Bytes object:", b)  #output: Bytes object: b'ABC'