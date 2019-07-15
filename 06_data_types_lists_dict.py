# Lists and Dictionaries
# List / Array

# Sometimes we just need to list our crazy pokemons
# because we dont want to work there

#This is how you make a list
# [] separate items using a comma
# declaring a list and saving to variable
crazy_pokemons = ['Snorlax','Jigglipuff','Mewtoo']
print (crazy_pokemons)
print (type(crazy_pokemons))

# Lists are organised using index
# Indexes start at 0

print(len(crazy_pokemons))
print(crazy_pokemons[0])
print(crazy_pokemons[2])

#if you want to print the last in a list
#you have two options
    #array [len(array) -1]
    #
print ('......')
print (crazy_pokemons[len(crazy_pokemons)-1])

print (crazy_pokemons[-1])

#Reassigning the value in a list using the index
# We need to evolve Mewtoo to Mewtree

crazy_pokemons[2] = 'Mewtree'
print (crazy_pokemons)

#Appending a new pokemon
# We caught Pigeoto
crazy_pokemons.append('Pigeoto')
print (crazy_pokemons)
#Inserting things to the list
crazy_pokemons.insert(0, 'Rattata') #The zero allows you to choose the location of insertion
print (crazy_pokemons)

#Removing a record using index
crazy_pokemons.pop()
print (crazy_pokemons)
crazy_pokemons.pop(1)
print (crazy_pokemons)

#Removing using a filter for a value

crazy_pokemons.remove('Rattata')
print (crazy_pokemons)

print('........................')
#Lists can have any data types
mixed_list = ['Jones',10,'42','John']
print (mixed_list)
print(type(mixed_list[0]), type(mixed_list[1]))

#Inception List
leo_d = ['first', 2 ,['leo','d']]
print (leo_d)
print (leo_d[0])
print (leo_d[2])
print (leo_d[2][1])

