# FILE HANDLING
""" Refers to the process of performing operations such as creating, opening, reading, writing and closing, also involves managing data flow between program and file system on storage devices. """

# OPENING A FILE -- open()
## Open the file and read its contents
#with open('Aviation.txt', 'r') as file:

# FILE MODES
""" 1. Read-only > opens file in reading mode, if file doesnt exists it throws and error
    2. read-only binary mode > opens file for reading binary data,if file doesnt exists it throws an error
    3. read and write mode > opens file for both reading and writing ,if file doesnt exists it throws an error
    4. read and write in binary mode > opens file for both reading and writing binary data, , if file doesnt exists it throws an error. 
    5. write mode > opens file for writing, creates new file or truncates existing file..
    6. write in binary mode > opens file for writing binary data,creates new file or truncates existing file..
    7. write and read mode > opens file for both reading and writing, creates new file or truncates existing file..
    8. write and read in binary mode > opens file for both reading and writing binary data, creates new file or truncates existing file..
    9. append mode > opens file for appending data, creates new file if it doesn't exist
    10. append in binary mode > opens file for appending binary data, creates new file if it doesn't exist
    11. append and read in binary mode > opens file for appending and reading the data, creates new file if it doesn't exist
    12. exclusive creation mode > creates new files, gives error if file already exists
    13. exclusive creation in binary mode > creates new binary file, gives error if file already exists
    14. exclusive creation with read and write mode > creates new file for reading and writing, gives error if file already exists
    15. exclusive creation with read and write in binary mode > creates new binary file for reading and writing, gives error if file already exists. """

# READING A FILE 
file = open("/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Aviation.txt", "r")
content = file.read()
print(content)
file.close()
""" O/P: FlightID,Departure,Arrival,Duration
AA101,New York,Los Angeles,6h
BA202,London,Paris,1h15m
DL303,Atlanta,Chicago,2h30m """

# READING IN BINARY MODE
file = open("/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Aviation.txt", "rb")
content = file.read()
print(content)
file.close()
""" O/P: b'FlightID,Departure,Arrival,Duration\nAA101,New York,Los Angeles,6h\nBA202,London,Paris,1h15m\nDL303,Atlanta,Chicago,2h30m\n' """

# WRITING A FILE
file = open("/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Cartoon Academy.txt", "w")
file.write("Hello, World!")
file.close()

# WRITING FILE IN APPEND MODE 
# Python code to illustrate append() mode
file = open('/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Cartoon Academy.txt', 'a')
file.write("Welcome to my Cartoon Academy...!")
file.close()

#CLOSING A FILE
with open("/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Cartoon Academy.txt", "r") as file:
    content = file.read()
    print(content)


# USING with STATEMENT --- Ensures that file is properly closed after its suite finishes, even if an exception is made this method automatically handles closing the file once the block of code is exited, even if error occurs. Reduces the risk of file corruption and resource leakage...
with open("/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Cartoon Academy.txt", "r") as file:
    content = file.read()
    print(content)
""" O/P: Hello, World!
         Welcome to my Cartoon Academy...!"""

#HANDLING EXCEPTIONS WHEN CLOSING A FILE
try:
    file = open("/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Cartoon Academy.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
""" O/P: Hello, World!
        Welcome to my Cartoon Academy...!"""

# tell() in FILE HANDLING - is a method of file objects that returns the current position of the file pointer (cursor) within the file. It returns an integer representing the byte offset from the beginning of the file where the next read or write operation will occur. 
# Open a file in read mode
file = open('/Users/venkatasrideepthisrikotapeetamabaram/Downloads/Cartoon Academy.txt', 'r')
# Read the first 10 characters
content = file.read(10)
print(content)
# Check the current position of the file pointer
position = file.tell()
print("Current position:", position)
# Close the file
file.close()
""" O/P: Hello, Wor
Current position: 10 """