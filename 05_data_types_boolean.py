#Booleans
#Boolean is a data type that is either true or false

# Syntax is capital letter
var_true = True
var_false = False

print(type(var_true))
print(type(var_false))

#When we equate / evaluate something we get a boolean as a response
#Logical operator return boolean
# == / != / <> / >=/ <=
weather = 'Rainy'

print(weather == 'Sunny')
print(weather == 'Rainy')

#Logical AND & OR
#AND - Evaluates two sides, and BOTH have to be true for it to return TRUE
print(True and True)
print(True and False)
print(weather =='Rainy' and True)
#OR - Evaluates two sides, either one has to be TRUE for it to return TRUE
print(True or False)
print(weather == 'Sunny' or weather =='Rainy')


# Some methods or functions can return booleans
potential_number = '10'
print ('..................')
print (potential_number.isnumeric())

text = 'Hello World!'
print(text.startswith('H'))
print(text.startswith('h'))
print(text.endswith('!'))
print(text.endswith('?'))
print (text[-1] == '!') #string are list of characters, -1 represents the last index in the said list.

#Booleans and numbers
print("printing boolean values of numbers")
print (bool(0))
print (bool (13))
print (bool(1))

#Value of None
print (bool(None))



