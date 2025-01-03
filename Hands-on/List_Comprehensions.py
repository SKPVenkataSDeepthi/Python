## list and list comprehensions are faster than using a for loop 

names = ["Scoobydo", "Bob", "Mr.Bean", "Mickey"]


names.append("Daisy") ## adding at the end of the list


names += ["Pluto"] ### similar to append... shorthand version 


names.extend(["Donald", "Mario", "Teddy"]) ### works on any iterables


names[len(names):] = ["Tweety", "Daffy Duck", "Bugs Bunny"] #### can also be added to the list by slicing operation 


names.insert(0, "Sylvester") ### inserts Sylvester at the beginning of the list


names.remove("Bob") ### removes Bob from the list 

cartoon_characters = names.pop(7) ### remove items by items.. will return the removed item
print(cartoon_characters)

print("Sylvester" + " appears " + str(names.count("Sylvester")) + " time(s)") #### if there are duplicates it counts for the occurances of them or else it says it appears for one time...

names.reverse() ### reverses the entire list..
print(names)

# Sorting
ChannelNumbers = ['Cartoon Network', 5,'Disney', 6, 7, 'CBN']
ChannelNumbers.sort(key=str)
print(ChannelNumbers)

names.sort()
print(names)#### sorts alphabetically

names.sort(reverse = True)
print(names) ### sorts alphabets in reverse order

names.sort(key = len)
print(names) ### sorts by the length of each name

import random
# Advanced List Comprehensions
rolls = [random.randint(1,20) for _ in names]


rolls_and_names = list(zip(names,rolls)) ### using zip() function I'm are combining rolls and names 
print(rolls_and_names)  ### returns output like 1st roll being paired with 1st name...

## Nested list comprehensions
top_rolls = [[random.randint(1,20) for _ in range(5)] for _ in names] ### each row rep top 5 rows for each person


top_rolls = [(names, [random.randint(1,20) for _ in range(5)]) for name in names] ### each row is a tuple of name and top 5 rows..
print(top_rolls)

