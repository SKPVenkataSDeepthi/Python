# variables -- containers to store values
# There is no need to declare a variable in python before its use

name = input("what is your name?")
print(name)
length = len(name)
print(length)


#swapping two numbers
A = input("Enter value of A: ")
B = input("Enter value of B: ")
temp  = A
A = B 
B = temp
print("A=" + A) ### Can also use "," in place of "+"
print("B=" + B) ### Can also use "," in place of "+"

""" VARIABLE NAMING RULES:
1. Variable should have meaningful name
2. Must start with either a letter or an underscore
eg., name, age, _age, id
3. Variable name can contain only alpha numeric characters(A-Z, a-z, 0-9) and underscore, no other special symbol is allowed. Spaces are also not allowed. 
eg., roll_no, student_id, length1
invalid variable names: eg., roll#no, 1s_name, roll number
4. Variable names are case sensitive. Python is case sensitive language.
eg., roll_no, Roll_No, roll_No --- all these are different 
5. Variables names should not be reserved words
6. Name can nnot begin with a digit
7. MULTI-WORDS VARIABLE NAMES:
7.1 Camel Case: each word except the 1st starts with a capital letter
eg., myAviationBookList
7.2 Pascal Case: each word starts with capital letter
eg., MyVAviationBookList
7.3 Snake Case: each word is seperated with an underscore
eg., my_aviation_book_list """



