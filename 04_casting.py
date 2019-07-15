# Casting is when you change the data type of an object
# We can cast strings into integers or integers into strings

# Casting String Class into Integer Class
number_string = '10'
print(type (number_string))
#At first 10 was a string, but the command below changed it into an integer.
number_int = int(number_string)
print (type(number_int))

# Casting integer class to string class
print ("Now let us do the same but for strings to integers")
number_int2 = 11
print(type(number_int2))
# Change to string using str()
number_int2_str = str(number_int2)
print (type(number_int2_str))

print ("This value is a", type(number_int2_str))
