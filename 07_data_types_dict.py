#Dictonaries AKA Hashes
# Work with key: value pairs.

#Declaring a hash / dictionary
pika = {}

# Dictionary work with keys: values
pika = {
    'name': 'Derik Dice',
    'pokemon': 'pickachu',
    'age': 17,
    'personality': 'Grumpy'}

print (pika)
print (type(pika))
# Access information using the keys.
print(pika['age'])
print(pika['pokemon'])

#Reassign values, using the keys
pika['age'] =18
print (pika['age'])

#Adding a key: value pair

pika['colour'] = 'Yellowish'
print(pika)

#Creating key value for first and last name
full_name = pika['name'].split()
print (full_name)
first_name = full_name[0]
print(first_name)
pika['first_name'] = first_name
pika['last_name'] = full_name[1]
print(pika)

#Embedded Data
pika = {
    'name': 'Derik Dice',
    'pokemon': 'pickachu',
    'age': 17,
    'personality': ['grumpy','jumpy','shocking', 'statics']}

print(pika['personality'])
print(pika['personality'][0])

pika = {
    'name': 'Derik Dice',
    'pokemon': 'pickachu',
    'age': 17,
    'personality': {
        'grumpy':10,
        'lovely':2}}

print(pika['personality']['grumpy'])

#Important Methods

print (pika.keys())

values = pika.values()
print (values)



