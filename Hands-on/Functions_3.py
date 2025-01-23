# RETURN
""" Return has 2 different variants 
1. Return without an expression
2. Return with an expression """

### Return without an expression 
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
happy_new_year() ### If we keep happy_new_year(False) it will only return Three.. Two...One.. as output
print("Happy New Year!")

### Return with an expression
def boring_function():
    return 123
x = boring_function()
print("The boring_function has returned its result. It's:", x)

def boring_function():
    print("'Boredom Mode' ON.")
    return 123
print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")


# NONE
# Its not a value, so it shouldnt take part in any expressions
""" print(None + 2) """ ## this will give error, TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

""" NOTE: NONE is a keyword 
NONE is used at 
1. Assigning to a variable
2. Comparing it with a variable"""

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1)) ### gives output as 2 and None

""" Can a list be sent to function as an argument ? Yes.."""

""" Can a list be a function result? Yes... """ 

# FUNCTION and SCOPES
""" SCOPE is the part of a code where the name is properly recognizable """
def scope_test():
    x = 123
scope_test()
print(x)

## variable existiing outside a function has scope inside the functions body
def my_function():
    print("Do I know that variable?", var)
var = 1
my_function()
print(var) #### o/p: Do I know that variable? 1 in next line we will get 1

def my_function():
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function()
print(var) #### o/p: Do I know that variable? 2 in next line we will get 1
""" result slightly changed because of using var variable inside the function and this is not same as var varaible which is used outside the function. As a result function variable shadows the variable coming from the outside world.""" 


""" Variable existing outside the function has scope inside the function's body, excluding those which define a variable of the same name. This is same as scope of variable existing outside of a function is supported only when getting its value. """

# FUNCTIONS AND SCOPES THE GLOBAL KEYWORD:
""" GLOBAL is a keyword --- this is to refrain from creating a new variable inside the function, the one accessible from outside will be used instead."""
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)
var = 1
my_function()
print(var) ### o/p: Do I know that variable? 2 in the next line it gives 2


""" 1. If argument is a list, then changing the value of the corresponding parameter doesn't affect the list
     2. If we change the list identified by the parameter the list will reflect the change."""


# QUESTIONS: 
## CODE 1:
"""def message():
    alt = 1
    print("Hello, World!")
print(alt)""" ##### O/P: Gives nameerror

## CODE 2:
a = 1
def fun():
    a = 2
    print(a)
fun()
print(a) 
## O/P: 2 in the next line it gives 1


## CODE 3:
a = 1
def fun():
    global a
    a = 2
    print(a)
fun()
a = 3
print(a)
## O/P: 2 in the next line gives 3

## CODE 4:
a = 1
def fun():
    global a
    a = 2
    print(a)
a = 3
fun()
print(a)
## O/P: 2 in the next line 2





