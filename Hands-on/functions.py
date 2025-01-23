## without invocation(calling a function.).... 
def message():
    print("Enter a value: ")
print("We start here.")
print("We end here.")


### we've inserted the function's invocation between the start and end messages:
def message():
    print("Enter a value: ")
print("We start here.")
message()
print("We end here.")

### ERROR 1: NameError: name 'message' is not defined -- It's because We've moved the function to the end of the code.Python will not be able to find it when the execution reaches the invocation..
""" print("We start here.")
message()
print("We end here.")
def message():
    print("Enter a value: ")""" 

### This code is correct 
print("We start here.")
def message():
    print("Enter a value: ")
message()
print("We end here.")
### The difference between the above two codes is the order of function definition and invocation in Python, in ERROR 1 code, the message() function is defined before it is invoked (called) (FUNCTION DEFINITION BEFORE INVOCATION). In the 2nd code, the message() function is called before it is defined (FUNCTION INVOCATION BEFORE DEFINITION)...
"""Functions must be defined before they are invoked because Python processes the function definitions sequentially.""" 

### You mustn't have a function and a variable of the same name.
def message():
    print("Enter a value: ")
message = 1
### Assigning a value to the name message causes Python to forget its previous role. The function named message becomes unavailable.


def message():
    print("Enter a value: ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

""" 1. input() is a built-in function """


""" 2. we get NameError when we try to invoke a function before we define it"""

""" ERROR 2: When executing the below code we will get TypeError, the hi() function doesn't take any arguments.
def hi():
    print("hi")
hi(5)




