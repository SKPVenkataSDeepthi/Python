# PARAMETERIZED FUNCTIONS
""" Parameter is a variable. 
Two important factors of parameters are:
1. Parameters exist only inside functions in which they have been defined.
def function(parameter):
    ### 
2.Assigning a value to the parameter is done at the time of the function's invocation"""

# Difference between parameters and arguments
""" Parameters: live inside the function
Arguments: exist outside the function. These are the carriers of values passed to corresponding parameters""" 

""" 1. Specifying one or more parameters in a function's definition is also a requirement
    2. Provide as many arguments as there are defined parameters. """

### ERROR: This below code gives TypeError: message() missing 1 required positional argument: 'number'
"""def message(number):
    print("Enter a number:", number)
message()"""

def message(number):
    print("Enter a number:", number)
message(1)
### Enter a number: 1 -- output

### SHADOWING --- variable named same as the functions parameter
def message(number):
    print("Enter a number:", number)
number = 1234
message(1)
print(number) 
""" Paramer 'x' shadows any variable of the same name but, only inside the function defining the parameter."""

#### shadowing with more parameters... we can use more parameters but it becomes difficult for remebering the role 
def message(what, number):
    print("Enter", what, "number", number)
message("telephone", 11)
message("price", 5)
message("number", "number")


# POSITIONAL PARAMETERS -- A technique which assigns the ith argument to the ith parameter is called positional paramter passing, arguments passed are called as positional arguments.

def my_function(a, b, c):
    print(a, b, c)
my_function(1, 2, 3) ### o/p: 1,2,3


def introduction(first_name, last_name): 
    print("Hello, my name is", first_name, last_name)
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent") ### o/p : Hello, my name is Luke Skywalker same way other 2 names are printed


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark") ### o/p : Hello, my name is Skywalker Luke  same way other 2 names are printed


###KEYWORD ARGUMENT PASSING --- The meaning of the argument is dictated by its name, not by its position this is called as keyword argument passing 

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke") ### o/p : Hello, my name is James Bond same way other 2 names are printed

##ERROR:TypeError: introduction() got an unexpected keyword argument 'surname', this is because we mustn't use a non-existent parameter name.
""" def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction(surname="Skywalker", first_name="Luke") """ 


### MIXING POSITIONAL AND KEYWORD ARGUMENTS --- To do this we have to put positional arguments before keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(1, 2, 3) ### invoking the function


# PARAMETERIZED FUNCTIONS - MORE DETAILS 
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
introduction()

def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction() ## o/p John Smith



























