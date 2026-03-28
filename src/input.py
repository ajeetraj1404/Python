# Taking user input from stdin buffer
a = input("Enter a value:") # By default it takes string from buffer
print(a,type(a))
# In order to get required input data
a = int(input("Enter a value:")) # Now after taking the string input int method will convert it to integer
print(a,type(a))
