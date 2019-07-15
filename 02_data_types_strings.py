#Data Types
# Computers are stupid.
# They dont understand context, and we need to be very specific with data types

#We can use type() to check datatypes

#Strings
    # Lists of characters bundled together in a specific order
    # using in


print ('Hello')
print (type ('hello'))

#Concatenation of strings - joining of two strings
string_a = 'hello there'
name_person = 'Juan Pier'
print(string_a + ' ' +  name_person)

#Useful methods
#Length
print (len (string_a))
print (len(name_person))

#Strip
    #Removes trailing white spaces
    #Removes spaces from the beginning and the end

string_num = '90383 '
print (type (string_num))
print (string_num)
print (string_num.strip())

#Split
#It splits in a specific location and outputs a list (data type)
string_text = "Hello, my name is Zaid, I like football"
split_string =string_text.split()
print (split_string)

#Count /Lower / Upper / Capitalize
text_example = "Here is sOMe text, with lots of text"
#Count
print (text_example.count('e'))
print (text_example.count('text'))

#Lower
print (text_example.lower())

#Upper
print (text_example.upper())

#Capitalize
print(text_example.capitalize()
print ('please give us a string to print')
user_input = input()
print (user_input)

#Get user input and print first and last name
# - get user to input first na,me
#- and save it to variable
first_name = input ('What is your first name?')
#- get user last name
# - and save it to a variable
last_name = input ('What is your last name?')
# - Join the two and let us concatenate
full_name  = first_name +' '+ last_name
print(full_name)

#let us use interpolation
welcome_message = f"Hi {full_name}, you are very welcome!"
print (welcome_message)


