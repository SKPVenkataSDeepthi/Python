# Boolean Expressions -- Evaluates either True or False, Used to check status codes or if user has entered correct password

print('1==1 is {}'.format(1==1)) ## return True

print('5==7 is {}'. format(5==7)) ## return false

x = 5
y = 7

print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x is y) ### x is same as y
print(x is not y) ### x is not same as y 
## "is" and "is not" is used to ref. the same object, but avoid comparing a value with a variable as it gives a warning

a = 5
b = 5
print(a and b) 
print(a or b)
print(not a)


a = 5
b = 6
print(a and b) ## true if both a and b are true -- returns a value 
print(a or b) ## true if either of a or b are true --- returns b value
print(not a) ### true if a is false
## Non zero numbers are considered as true


d = 6
if not d%3 and not d%2:
    print("Sky Captain")

d = 6
if d%3 == 0:
    print("Aviator")
if d%2 == 0:
    print("Wingman")



## Conditional Execution
if condition:
    ## execution logic 

if condition:
    ## execution logic 
elif condition:
    ## execution logic: if 1st condition is not met
else:
    ## execution logic: if all other conditions are false 

## switch statements -- conditional statement that allows us to check a variable against a series of values
match variable:  ### match does not have a break statement
   case value1:
       ## execution logic: if variable = value1
   case value2:
       ## execution logic: if variable = value2
   case _:
     ## execution logic: if none of the previous conditions are met"""

cartoon = input("What is your favorite cartoon? ")

match cartoon:
    case "SpongeBob SquarePants":
        print("Who lives in a pineapple under the sea? SpongeBob SquarePants!")
    case "Tom and Jerry":
        print("Classic! The ultimate cat and mouse duo.")
    case "Looney Tunes":
        print("That's all, folks!")
    case "Dragon Ball Z":
        print("Powering up to over 9000!")
    case "Pokémon":
        print("Gotta catch 'em all!")
    case _:
        print("That's a great choice! Cartoons bring out the kid in all of us!")

cartoon = input("What is your favorite cartoon? ")

match cartoon:
    case "SpongeBob SquarePants" | "spongebob squarepants" | "Spongebob":
        print("Who lives in a pineapple under the sea? SpongeBob SquarePants!")
    case "Tom and Jerry" | "tom and jerry":
        print("Classic! The ultimate cat and mouse duo.")
    case "Looney Tunes" | "looney tunes":
        print("That's all, folks!")
    case "Dragon Ball Z" | "dragon ball z" | "DBZ" | "dbz":
        print("Powering up to over 9000!")
    case "Pokémon" | "pokemon" | "Pokemon":
        print("Gotta catch 'em all!")
    case _:
        print("That's a great choice! Cartoons bring out the kid in all of us!")


## Iterations -- allow us to execute a block of code for multiple times, until the condition is met

# for loop --- iterate over a sequence of items (for each loop)
for item in sequence:
    # execution logic"""

for i in range(5):
    print(i)

# while loop: -- will execute a block of code until the condition is met
while condition:
    #execution logic"""







