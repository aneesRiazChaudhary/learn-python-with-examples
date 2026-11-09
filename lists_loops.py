# lists_loops.py  

"""
Topic: Lists and Loops

Concepts Covered:

1. Lists
   - Store multiple values in a single variable.
   - Maintain the order of stored items.

2. List Indexing
   - Access individual elements using indexes.
   - List indexes start from 0.

3. Accessing List Items
   - Retrieve values using square brackets [].
   - Example: my_list[1]

4. Iterating Through Lists
   - Use for loops to visit every item in a list.
   - Process list elements one at a time.

5. Loop Variables
   - Store the current item during iteration.
   - Improve readability and data access.

6. range() Function
   - Generate sequences of numbers.
   - Commonly used for counting and indexing.

7. len() Function
   - Determine the number of items in a list.
   - Frequently used with range().

8. Index-Based Iteration
   - Access list elements through their positions.
   - Useful when both indexes and values are needed.

9. Displaying Indexes and Values
   - Print both the position and content of list items.
   - Helpful for reporting and debugging.

10. Human-Friendly Numbering
    - Convert zero-based indexes into one-based numbering.
    - More meaningful for users.

Key Takeaways:

- Lists store collections of related data.
- Indexes begin at 0 in Python.
- for loops are the most common way to process list items.
- len() returns the total number of elements.
- range(len(list)) allows access to item positions.
- User-friendly numbering often starts at 1 rather than 0.
"""

student_list = ["s1", "s2", "s3"]
#  this will print the value of the entered index
print(student_list[1])


# this will print out all students from the list 
for student in student_list:
    
    print(student)
    
    
    
    
# if we ant to itrate over a list of items we can not directly use range we will use len of list as an argument of range

subj_list = ["phy", "chem", "eng", "maths"]

for item in range(len(subj_list)):
    print(subj_list[item])
    
    

print("list items along with their index starting from zero")

field_list = ["science", "arts", "designer", "wella"]
# printing list items along with their index 
for item in range(len(field_list)):
    # this will print index zero to last index
    print(item, subj_list[item]) 
   
    
    
# print list items along with their index but instead of 0 we will make correct behaviour index 1 not zero 

print("list item along with index starting from item 1 to last")

list_countries = ["Pak","afg","iran","iraq","uae"]

for i in range(len(list_countries)):
    print(i+1, list_countries[i])
    
    

    