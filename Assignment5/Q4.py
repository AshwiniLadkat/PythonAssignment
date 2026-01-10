#predict the output
ba = bytearray([65, 66, 67])
ba[0]=97
print(ba) 
# Output will be bytearray(b'aBC')
# Why does this allowed ?
  #bytearray is  mutable, so we can change its content after creation.
