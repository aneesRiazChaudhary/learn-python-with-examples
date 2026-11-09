# intro.py  

"""
Topic: Python Introduction and String Manipulation

Concepts Covered:

1. Variables
   - Store data inside named containers.
   - Reuse information throughout a program.

2. User Input
   - Collect information from users using input().
   - Store input inside variables.

3. String Data Type
   - Work with textual information.
   - Perform various string operations.

4. Whitespace Removal
   - Use strip() to remove leading and trailing spaces.
   - Helps clean user input.

5. Capitalization Methods
   - capitalize() makes only the first character uppercase.
   - title() capitalizes the first letter of each word.

6. Method Chaining
   - Combine multiple string methods together.
   - Example: strip().title()

7. Formatted Strings (f-strings)
   - Insert variables directly into strings.
   - Create readable and dynamic output.

8. Escape Characters
   - Use \\n to create a new line.
   - Improve output formatting.

9. Input Processing
   - Clean and format user input immediately.
   - Reduce the need for additional processing later.

10. String Splitting
    - Use split() to divide text into multiple values.
    - Store separated values into individual variables.

11. Multiple Variable Assignment
    - Assign multiple values at once.
    - Useful when working with split strings.

Key Takeaways:

- User input is received as text by default.
- String methods help clean and standardize data.
- Method chaining makes code shorter and more readable.
- f-strings provide a modern way to format output.
- split() allows extraction of specific parts of text.
- Proper input handling improves user experience and data quality.
"""


name = input("Enter your name: ")
# remove white space from a str it will strip white soace fron keft and right of a string
name = name.strip()
# captalization this will captalize first letter only before space 
# name = name.capitalize()
# while with title we can captalize other parts after soace too 
name = name.title()



#  we can cobine string and captalization togather 
name = name.strip().title()
age = input ("Enter Your Age: ")
print(f"My name is, {name} \n My age is: {age}" )



# a better approach is striping and captalization of at the time of input 

father_name = input("enter your father name:").strip().title()
print(f"my father name is: {father_name}") 


#  split function
Designation = input("please enter your designation").strip().title()
first, last = Designation.split(" ")
print(f"dear {last}")