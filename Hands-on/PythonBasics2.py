###SETS###
set = set(["Scooby", "Dooby"])
print(set)

set.add("Doo")
print(set)

#sets doesnot support item assignment
##set[1] = "Show" ---> this will give error as 'set' object does not support item assignment
##print(set)

# sets can store different datatypes
myset = {"Scooby", "Dooby", "Doo", 5,7,True, 0.57}
print(myset)

#Frozen Sets
# These are immutable objects while elements of a set can be modified at any time, elements of frozen set remain the same after creation.
# If no parameters are passed then it returns an empty frozen set.
frozenset_set = frozenset(["e","f","g"])
print(frozenset_set)

#Internal working ---> this is based on data structure called as hash table.
#If we have multiple values present at same position then the values is appended to that index position to form a linked list.

#Methods in sets
#1. Adding elements to sets
characters = {"Rogers", "Scrappy-Doo", "Scooby-Dum"}
print(characters)
characters.add("Dinkley")
print(characters)

people = {"Mr. Bean", "Irma Gobb","Mrs. Wicket"}
pets = {"Teddy", "Scrapper"}
all_char = people.union(pets)
print(all_char)

#union using '|' operator
all_char = people|pets

#Itersection operator
all_char = people.intersection(pets)
print(all_char)

#Intersection using '&' operator
all_char = people & pets

#clearing the sets
show = {"Strawberry Shortcake", "Blueberry Muffin","Raspberry Tart", "Lemon Meringue"}
show.clear()
print(show)

####Dictonaries#####
# it stores the value in key:value pairs
dict = {1: 'Tom', 2:'Jerry', 3:'Spike'}
print(dict)

dicta = {'Name':'Tom & Jerry', 1:[1,2]}
print(dicta) ## prints with use of mixed keys



