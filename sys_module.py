# sys_module.py


"""
Topic: The sys Module and Command-Line Arguments

Concepts Covered:

1. Importing Modules
   - Use import to access Python's built-in modules.
   - The sys module provides access to interpreter features.

2. User Input vs Command-Line Input
   - Traditional programs use input().
   - Command-line arguments allow input during program execution.

3. sys.argv
   - A list containing command-line arguments.
   - Stores information entered after the script name.

4. Understanding argv Indexes

   sys.argv[0]
   - Contains the script filename.

   sys.argv[1]
   - First user-provided argument.

   sys.argv[2]
   - Second user-provided argument.

5. Accessing Command-Line Arguments
   - Retrieve values directly from argv.
   - Avoid prompting users with input().

6. IndexError
   - Occurs when attempting to access an argument that was not provided.
   - Common when working with sys.argv.

7. Exception Handling
   - Use try-except blocks to catch missing arguments.
   - Prevent unexpected program crashes.

8. Argument Validation
   - Use len(sys.argv) to verify the required number of arguments.
   - Ensure users provide sufficient input.

9. Conditional Validation
   - Detect missing or excessive arguments.
   - Display meaningful feedback messages.

10. sys.exit()
    - Immediately stop program execution.
    - Provide user-friendly error messages.

11. List Slicing

    sys.argv[1:]

    - Skip the script name.
    - Process only user-provided arguments.

12. Iterating Through Arguments
    - Use loops to process multiple command-line values.
    - Useful for automation and scripting.

Key Takeaways:

- sys.argv stores command-line arguments.
- The script name is stored at index 0.
- Missing arguments can raise IndexError.
- len(sys.argv) helps validate input.
- sys.exit() provides cleaner error handling.
- Command-line arguments are commonly used in automation and scripting.
"""

import sys 


user_name = input("enter user_name")
print(user_name)

# instead of above code we can use sys.argv to take user in terminal when we run file we will write usename along with fileadress/file_name.py user_name then enter 

print("#"*20, "intead if creating and returning user input tags, we will use sys module to get user unput")
# argv is a veriable availble in sys module that caputres list of human typed prompt or information data 
# usingsys.orgv we will take user input without initializing an input and return value we will simply take user ibput with sys.argv
# on runing file in terminal we will directly wirte the desired information such as user name along with file nama . for our case in terminal adress tofile/sys_module.py Haider

# if we excute in terminal without providing desired input it will riase an indexError
# when we use [0] then we can skip user_name without any error, if we use [1] then we must provide desired input along wth file name 
print("hello,I am,", sys.argv[1]) 

print("#" * 20, "new section", "error handling")

try:
    print("my profession is:", sys.argv[2])
    # this time we will pass two arguments in terminal along with file_adress/file_name.py user_name user_profession
except IndexError:
    print("please provide your profession")
    
print("#" * 20, "new section", "error handling with if else switch")
# intead of try except we will make validation at input time with if else

if len(sys.argv) < 3:
    print("insufficient data provided")
elif len(sys.argv) >3:
    print("too many arguments")
    
else:
    print("I am from Pakistan", sys.argv[2])
    
    
    
print("#" * 20, "new section", "sys.exit")
# sys.exit offer baetter error handling 

if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) >2:
    sys.exit("too many arguments")
    
# print("heloo", sys.argv[1])
for arg in sys.argv[1:]:
    print("hello ,i am ",arg)

    