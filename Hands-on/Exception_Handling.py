# PYTHON EXCEPTION HANDLING
""" 1. This handles errors that occur during execution of program. 
    2. Instead of crashing the running program, it allows to respond to the error
    3. It allows to catch and manage errors."""

# Example of an IndexError
my_list = [1, 2, 3, 4, 5]
try:
    # This will raise an IndexError because index 10 does not exist
    value = my_list[10]  
except IndexError:
    print("Index out of range!")
""" The try block contains the code that might cause an exception and the except block handles the exception, printing an error message instead of stopping the program."""

# ERROR Vs EXCEPTION
""" ERROR : Serious issue that a program should not try to handle 
EXCEPTION : Less severe than errors and can be handled by the program """

# SYNTAX
""" try: [Python will “try” to execute the code in this block. If an exception occurs, execution will immediately jump to the except block.]
      # Code that might raise an exception
except SomeException: [Python jumps to the except block and executes it. We can handle specific exceptions or use a general except to catch all exceptions.]
      # Code to handle the exception
else: [is optional and if included, must follow all except blocks. The else block runs only if no exceptions are raised in the try block.]
     # Code to run if no exception occurs
finally: [always runs, regardless of whether an exception occurred or not.]
    # Code to run regardless of whether an exception occurs"""

try:
    num = int(input("Enter a number: "))  # Could raise a ValueError
    res = 50 / num  # Could raise a ZeroDivisionError
except ZeroDivisionError:
    print("Division by zero is not allowed!")  
except ValueError:
    print("Please enter a valid integer!")   
else:
    print("Result is:", res)   
finally:
    print("Execution complete.")


# COMMON EXCEPTIONS IN PYTHON
""" 1. BaseException -- Base class for built-in exceptions
    2. Exception -- base class for all non-exit exceptions
    3. ArithmeticError -- base class for all errors related to arithmetic operations
    4. ZeroDivisionError -- raised when division or module operation is performed with zero as divisor
    5. OverflowError -- raised when numerical operation exceeds maximum limit of a data type
    6. FloatingPointError -- raised when floating point operation fails 
    7. AssertionError -- raised when assertion fails
    8. AttributeError -- raised when attribute reference or assignment fails 
    9. IndexError -- raised when sequence script is out of range
    10. KeyError -- raised when dictonary key is not found
    11. MemoryError -- raised when operation runs out of memory 
    12. NameError --- raised when local or global name is not found
    13. OSError --- raised when system related operation fails 
    14. TypeError -- raised when an operation or function is applied to an object of inappropriate type
    15. ValueError -- raised when a function receives an argument of the right type but inappropriate value. 
    16. ImportError -- raised when import statement has issues
    17. ModuleNotFoundError --- raised when module cant be found."""


# CATCHING EXCEPTIONS --- This makes code to respond to different exception types differently
try:
    # Attempting to open a file that doesn't exist
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist!")
except PermissionError:
    print("You do not have permission to access this file!")
else:
    print("File content:", content)   
finally:
    print("File operation attempted.")
## o/p :The file does not exist! 



# CATCHING MULTIPLE EXCEPTIONS --- We can catch multiple exceptions in single block if we need to handle them in same way or we can seperate them if different types of exceptions require different handling. 
data = [1, 2, 3, 4]
try:
    # Trying to access an invalid index and perform division
    result = data[5] / 0  # IndexError first, but ZeroDivisionError won't be reached
    
except (IndexError, ZeroDivisionError) as e:
    print("An error occurred:", e)

else:
    print("Result is:", result)

finally:
    print("Execution complete.")
#O/P: File operation attempted.
# An error occurred: list index out of range
# Execution complete.

# CATCHING ALL HANDLERS
try:
    # Simulate risky calculation: dividing by zero
    num = int(input("Enter a number: "))  # Could raise ValueError
    res = 10 / num  # Could raise ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")   
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Result is:", res)  
finally:
    print("Execution complete.")
""" O/P: Enter a number: 45
Result is: 0.2222222222222222
Execution complete.
Enter a number: 0
You can't divide by zero!
Execution complete.
Enter a number: 5.67
Please enter a valid number!
Execution complete. """




