#!/usr/bin/env python
# coding: utf-8

# Refference from Leetcode, Geeks for Geeks, Narasimha Karumanchi-Data Structure and Algorithmic Thinking with Python  Data Structure and Algorithmic Puzzles-Careermonk Publications (2016)

# # STACKS
# 
# * It is an ordered collection of elements. They are added and removed from the end. Ex: Plates iin kitchen. 
# 
# * LIFO - Last In First Out - Last element placed is the 1st one to come out. 
# 
# * Any dynamic array can implement stacks.
# 
# **Array operations are as follows:**
# 
# * Pushing - inserting element into the stack. 
# 
# * Popping - removing element from the stack. 
# 
# * Peek - looking at the top of the stack. 
# 
# * top() - returns top element
# 
# * isEmpty() - returns true if stack is empty else false
# 
# * isFull() - returns true if stack is full else false.
# 
# 

# **Algorithm for Push Operation:**
# 
# 1. Before Pushing element into the stack check if stack is full. 
# 2. If the stack is full, we cant insert the element as it is overflow condition. (top == capacity -1). 
# 3. If the stack is not full, we increment the value of top by 1 and new value is inserted at the top. (top = top+1)

# **Algorithm for Pop Operation:**
# 1. Before popping the element from the stack, check if the stack is empty or not. 
# 2. If the stack is empty,we canot remove any elements further as it is stack underflow condition. (top == -1)
# 3. If the stack is not empty we store value on the top, decrement the value of top by 1 and return top stored value. (top = top -1)
# 
#     

# **Algorithm for Top/Peek Operation:**
# 1. Before returning the top element from the stack, we check if the stack is empty.
# 2. If the stack is empty, we simply print “Stack is empty”.(top == -1)
# 3. Otherwise, we return the element stored at index = top .

# **Algorithm for isEmpty Operation:**
# 1. Check for the value of top in stack.
# 2. If (top == -1) , then the stack is empty so return true .
# 3. Otherwise, the stack is not empty so return false .

# **Algorithm for isFull Operation:**
# 1. Check for the value of top in stack.
# 2. If (top == capacity-1), then the stack is full so return true.
# 3. Otherwise, the stack is not full so return false.

# # Applications
# 
# 1. Infix to Postfix conversions
# 2. Redo/ Undo features
# 3. Forward/ Backward features in web browsers. 

# # Types of Stack data structures
# * Fixed Size Stack: It has fixed size and cannot grow or shrink dynamically. 
# 
# * Stackoverflow: If stack is full and if you try to add element to it then it is called overflow. 
# 
# * Underflow: If stack is empty and if you try to remove elements from that an underflow occurs. 
# 
# * Dynamic Size Stack: It can grow or shrink dynamically. If statck is full it will increase its size automatically, and if stack is empty it will decrease size automatically. 
# 
# * Dynamic size stacks are implemented using Linked lists, as linked lists allows easy resizing of the stack. 

# # Stack Operations

# In[1]:


# Declaring a slack 
stack = []

#Pushing elements
stack.append(1)
stack.append(2)
stack.append(3)

stack


# In[2]:


#Popping elements
stack.pop() # for this it pops 3
stack.pop() # for this it pops 2
#stack.pop() # for this it gives error "pop from empty list" since the stack became empty


# In[3]:


#check if slack is empty or not 
not stack


# In[4]:


#Checking for element at top 
stack[-1]


# In[5]:


#get size of stack
len(stack)


# # Using stacks with strings: 
# 
# * Iterating over string and putting characters over stack
# 
# * Comparing top of stack with current character at each iteration
# 
# * Matching strings, as it has history of previous characters. 

# QUESTION:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The string is valid if all open brackets are closed by the same type of closing bracket in the correct order, and each closing bracket closes exactly one open bracket.
# 
# For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.

# In[6]:


class Solution:
    def isValid(self,s):
        stack = []
        matching = {"(": ")", "[":"]","{":"}"}
        
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                previous_opening = stack.pop()
                if matching[previous_opening] != c:
                    return False
        return not stack
    
s = "({})"
solution_instance = Solution()
print(solution_instance.isValid(s))


# # Remove All Adjacent Duplicates In String
# 
# QUESTION:
# You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.
# 
# For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.

# In[7]:


class Solution:
    def removeDuplicates(self, s):
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)
        
s = "abbaca"
solution_instance = Solution()
print(solution_instance.removeDuplicates(s))


# # Backspace String Compare
# 
# QUESTION:
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# 
# For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".

# In[8]:


class Solution:
    def backspaceStrCompare(self,s,t):
        def build(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
                    
            return "". join(stack)
        return build(s) == build(t)
    
s = "ab#c"
t = "ad#c"
solution_instance = Solution()
print(solution_instance.backspaceStrCompare(s,t))
    


# QUESTION:
# Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.
# 
# In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.
# 
# The simplified canonical path should adhere to the following rules:
# 
# It must start with a single slash '/'.
# Directories within the path should be separated by only one slash '/'.
# It should not end with a slash '/', unless it's the root directory.
# It should exclude any single or double periods used to denote current or parent directories.
# Return the new path.
# 
# Input: path = "/home/"
# 
# Output: "/home"
# 
# Explanation:
# 
# The trailing slash should be removed.

# In[9]:


class Solution(object):
   def simplifyPath(self, path):
       stack = []
       components = path.split('/')
       
       for comp in components:
           if comp == '..':
               if stack:
                   stack.pop()
           elif comp and comp != '.':
               stack.append(comp)
       
       simplified_path = '/' + '/'.join(stack)
       
       return simplified_path

solution = Solution()
print(solution.simplifyPath("/home/")) 
print(solution.simplifyPath("/home//foo/"))


# QUESTION:
# Given a string s of lower and upper case English letters.
# 
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
# 
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# 
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# 
# Notice that an empty string is also good.
# 
#  
# 
# Example 1:
# 
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
# 
# Example 2:
# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""

# In[10]:


class Solution(object):
    def makeGood(self,s):
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
solution_instance = Solution()
print(solution_instance.makeGood("leEeetcode"))
print(solution_instance. makeGood("abBAcC"))


# # Removing Stars from the String
# QUESTION:
# You are given a string s, which contains stars *.
# 
# In one operation, you can:
# 
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# 
# Note:
# 
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
#  
# 
# Example 1:
# 
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
# 
# Example 2:
# 
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
# 

# In[11]:


class Solution:
    def removeStars(self, s):
        stack = []
        for c in s:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)
        
s = "leet**cod*e"
solution_instance = Solution()
print(solution_instance.removeStars(s))  # Output should be "lecoe"


# QUESTION:
# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
# 
# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.
# 
#  
# 
# Example 1:
# 
# Input: s = "zza"
# Output: "azz"
# Explanation: Let p denote the written string.
# Initially p="", s="zza", t="".
# Perform first operation three times p="", s="", t="zza".
# Perform second operation three times p="azz", s="", t="".
# 
# Example 2:
# 
# Input: s = "bac"
# Output: "abc"
# Explanation: Let p denote the written string.
# Perform first operation twice p="", s="c", t="ba". 
# Perform second operation twice p="ab", s="c", t="". 
# Perform first operation p="ab", s="", t="c". 
# Perform second operation p="abc", s="", t="".
# 
# Example 3:
# 
# Input: s = "bdda"
# Output: "addb"
# Explanation: Let p denote the written string.
# Initially p="", s="bdda", t="".
# Perform first operation four times p="", s="", t="bdda".
# Perform second operation four times p="addb", s="", t="".
#  

# In[12]:


class Solution:
    def robotWithString(self, s):
        t = []
        result = []
        min_char_right = [None] * len(s)
        min_char = 'z'
        for i in range(len(s) - 1, -1, -1):
            min_char = min(min_char, s[i])
            min_char_right[i] = min_char

        for i, char in enumerate(s):
            t.append(char)
            while t and (i == len(s) - 1 or t[-1] <= min_char_right[i + 1]):
                result.append(t.pop())
        while t:
            result.append(t.pop())

        return ''.join(result)

solution_instance = Solution()

print(solution_instance.robotWithString("zza")) 
print(solution_instance.robotWithString("bac"))  
print(solution_instance.robotWithString("bdda")) 


# QUESTION:
# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
# 
#  
# 
# Example 1:
# 
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:
# 
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#  

# In[13]:


class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        pop_index = 0
        
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return not stack

solution_instance = Solution()
print(solution_instance.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))  
print(solution_instance.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))


# QUESTION:
# We are given an array asteroids of integers representing asteroids in a row.
# 
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# 
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# 
# Example 1:
# 
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# 
# Example 2:
# 
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# 
# Example 3:
# 
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# 

# In[14]:


class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        return stack

solution_instance = Solution()

print(solution_instance.asteroidCollision([5,10,-5]))  
print(solution_instance.asteroidCollision([8,-8]))      
print(solution_instance.asteroidCollision([10,2,-5]))   


# In[15]:


# Reverse a string of the stack

class Stack:
    def __init__(self):
        self.MAX_SIZE = 101
        self.a = [''] * self.MAX_SIZE
        self.top = -1

    def push(self, ele):
        if self.is_full():
            raise IndexError("Stack overflow")
        self.top += 1
        self.a[self.top] = ele

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        ele = self.a[self.top]
        self.top -= 1
        return ele

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top >= self.MAX_SIZE - 1

if __name__ == "__main__":
    original_string = "Hello, World!"
    string_length = len(original_string)
    stack = Stack()
    for i in range(string_length):
        c = original_string[i]
        stack.push(c)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    print(reversed_string)


# # Implement Stack Using Singly Linked List
# 
# Advantage of using linked lists in stacks is we can implement a stack that can grow or shrink as much as needed. But if you use an array it will put restriction on maximum capacity. 
# 
# **Push Operation**
# 1. Initialise a node
# 2. Update the value of that node by data i.e. node->data = data
# 3. Now link this node to the top of the linked list
# 4. And update top pointer to the current node
# 
# **Pop Operation**
# 1. First Check whether there is any node present in the linked list or not, if not then return
# 2. Otherwise make pointer let say temp to the top node and move forward the top node by 1 step
# 3. Now free this temp node
# 
# **Peek Operation**
# 1. Check if there is any node present or not, if not then return.
# 2. Otherwise return the value of top node of the linked list
# 
# **Display Operation**
# 1. Take a temp node and initialize it with top pointer 
# 2. Now start traversing temp till it encounters NULL
# 3. Simultaneously print the value of the temp node
# 

# In[22]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None #head by default is none

        #Now check if stack is empty or not
    def isempty(self):
        return self.head is None
     #Now we have to add (push) data to the stack if it is not empty   
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
    #Now we have to remove (pop) the element that is the current head        
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
    #Return the head node data (peek)    
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
        
    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack underflow")
        else:
            while iternode is not None:
                print(iternode.data, end="")
                iternode = iternode.next
                if iternode is not None:
                    print(" -> ", end="")
            print()  

if __name__ == "__main__":
    MyStack = Stack()
   
    MyStack.push(11)
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
 
    # Display stack elements
    MyStack.display()
 
    # Print top element of stack
    print("Top element is", MyStack.peek())
 
    # Delete top elements of stack
    MyStack.pop()
    MyStack.pop()
    
    # Display stack elements after popping
    MyStack.display()


# In[ ]:




