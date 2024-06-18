#!/usr/bin/env python
# coding: utf-8

# # List and List Comprehensions
# 
# * These are faster than using a for loop 
# 

# In[1]:


names = ["Naomi", "James", "Amos", "Bobbie"]
names


# In[2]:


names.append("Alex")
names


# In[3]:


names.extend(["Alfred", "Dawes", "Jacob"])
names


# In[4]:


names.extend("Nobel")
names


# In[5]:


names+=["bishop"]
names


# In[6]:


names.insert(0,"Holden")
names


# In[7]:


names.remove("Holden")
names


# In[8]:


names.remove("Amos")
names


# In[9]:


astronaut = names.pop(5)
print(astronaut + "is on his way to space")


# In[10]:


print("Naomi" + " " +"appears" + " " +str(names.count("Naomi")) + "times(s)")


# In[11]:


names.reverse()
names


# In[12]:


names_copy = names.copy()
names #this creates a shallow copy of a lsit


# # Sorting
# * A list can be sorted by calling the sort function. Sorting a list means that modifying the original list.
# 
# * Incase of a mixed types of list, a custom key function can be passed to the sort function. It is called on each element of the list, and the value returned is used to sort the list. 

# In[13]:


list = ['abc', 5,7,'def']
list.sort(key = str)
list


# In[14]:


list = [5,7,0.87,3.47,57,10.28]
list.sort(key = float)
list


# In[15]:


names.sort()
names #prints names in ascending order)


# In[16]:


names.sort(reverse = True)
names


# # Python Numbers
# * Integers  --> whole number, including negative numbers but not fractions. 
# * Float --> real number with floating point rep. 
# * Type Conversions
# * Decimal Numbers

# In[17]:


num = -8
print(type(num))


# In[18]:


#performing arithmetic operations
a = 5
b = 7

# Addition
c = a + b
print("Addition:",c)

d = 5
e = 7

# Subtraction
f = d - e
print("Subtraction:",f)

g = 5
h = 7

# Division
i = g // h
print("Division:",i)

j = 5
k = 7

# Multiplication
l = j * k
print("Multiplication:",l)

m = 5
n = 7

# Modulus
o = m % n

print("Modulus:",o)

p = 5
q = 7

# Exponent
r = p ** q
print("Exponent:",r)


# In[19]:


num = 5/7
print(type(num))


# In[20]:


num = 5 * 7.0

print(type(num))


# In[21]:


num = 5//7
print(type(num))


# In[22]:


a = 5.7
b = 7.5

# Addition
c = a + b
print("Addition:", c)

# Subtraction
c = a-b
print("Subtraction:", c)

# Division
c = a/b
print("Division:", c)

# Multiplication
c = a*b
print("Multiplication:", c)


# In[23]:


num = 5 + 7j
print(type(num))


# In[24]:


a = 7 + 5j
b = 6 + 7j

# Addition
c = a + b
print("Addition:",c)

d = 7 + 5j
e = 6 - 7j

# Subtraction
f = d - e
print("Subtraction:",f)


g = 7 + 5j
h = 6 + 7j

# Division
i = g / h
print("Division:",i)


j = 7 + 5j
k = 6 + 5j

# Multiplication
l = j * k
print("Multiplication:",l)


# # Type Conversion
# 
# We can convert one number into other form in 2 ways:
# 1. Using arithmetic operations
# 2. Using built-in functions
# 

# In[25]:


a = 7.6
b = 5

c = a + b

print(c)


# In[26]:


a = 7
print(float(a))

b = 5.6
print(int(b))

c = '7'
print(type(int(c)))

d = '5.6'
print(type(float(c)))

e = 7
print(complex(e))

f = 6.5
print(complex(f))


# # Strings

# In[27]:


string = "Aviation for life"
print(string)
print(type(string))


# In[28]:


#String with single quotes
String1 = 'Aviation for life'
print("String with Single Quotes: ")
print(String1)

# String with double Quotes
String1 = "I'm a foodie"
print("\nString with Double Quotes: ")
print(String1)

# String with triple Quotes
String1 = '''I love food I live in a world of "Geeks"'''
print("\nString with Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Aviation
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)


# In[29]:


String1 = "LiveOneLife"
print("Initial String: ", String1)

# Printing First character
print("First character of String is: ", String1[0])


# In[30]:


String1 = "LiveOneLife"
print("Initial String: ", String1)

# Printing Last character
print("Last character of String is: ", String1[-3])


# In[31]:


# Creating a String
String1 = "Code and chill"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(String1[3:-2])


# In[32]:


str = "Need more coffee"
print(str[::-1]) #rev a string


# In[33]:


gfg = "Works for me"

# Reverse the string using reversed and join function
gfg = "".join(reversed(gfg))

print(gfg)


# In[34]:


# delete a String

String1 = "Hakuna matata, no worries"
print("Initial String: ")
print(String1)

String2 = String1[0:2] + String1[3:]
print("Deleting character at 2nd Index: ")
print(String2)


# In[35]:


# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Live', 'Love', 'Laugh')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Live', 'Love', 'Laugh')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{u} {o} {l}".format(l='Live', o='Love', u='Laugh')
print("\nPrint String in order of Keywords: ")
print(String1)


# In[36]:


# Formatting of Integers
String1 = "{0:b}".format(8)
print("\nBinary representation of 8 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(5/7)
print("\ five by seventh is : ")
print(String1)


# # Tuples
# 
# * Placing sequence of values seperated by a comma with or without use of parentheses for grouping data
# * If we are creating tuples without the use of paranthesis then it is called as Tuple packing. 
# 

# In[37]:


Tuple = ()
Tuple


# In[38]:


#tuples with strings
tuple = ('Code', 'Zombie')
print("\nTuple using strings:")
tuple

