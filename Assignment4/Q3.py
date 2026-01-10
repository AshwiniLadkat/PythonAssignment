#Predict the output 

lst = [10,20,30]
tpl= (10,20,30)

lst[0]=100
tpl[0]=100  # This will raise a TypeError since tuples are immutable
print("List after modification:", lst)
print("Tuple after modification:", tpl)
# Output 
    #List after modification: [100, 20, 30]
    #TypeError: 'tuple' object does not support item assignment

