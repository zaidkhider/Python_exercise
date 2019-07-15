# Numericals - Integers, big integers, complex numbers

# Whole numbers (integers)
my_int = 13
print (type(my_int))

print (13)
print (type(13)) #Not the same as print (type('13'))

# Floats are composite numbers
print (13.1)
print (type(13.1))

# Long and complex
# Less used check when needed

#Operators

num_a = 10
num_b = 7

num_sum = num_a + num_b
print (num_sum) #Addition

num_sub = num_a - num_b
print (num_sub) #Subtraction

print (num_b*num_a) #Multiply

print (num_a/num_b) #Divide

#Modulus ---> check for remainders
print (10 % 2)
#Check if even
print ((12%2) == 0)
print (18%3)

#Logical Operators
# Check if equal ==
a = 10
b = 13
print (a == b) # Evaluates two sides and returns a boolean
print (a ==10)

# Checking if bigger and smaller than
print (a >b)
print (a > 9)
print ('.....')

print (b < a)
print (b < 15)

#Checking bigger/smaller or equal

print (a > 10)
print (a>=10)

#Check if not something

print (a != 9) # a is not 9, hence the answer is TRUE


#Increment
counter = 0
counter += 1 #putting a 1 means it will add 1 to the counter
print (counter)
counter += 1
print (counter)
