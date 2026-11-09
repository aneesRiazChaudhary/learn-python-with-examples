# exceptions.py
"""
Topic: Exception Handling

Concepts Covered:

1. Syntax Errors
   - Errors caused by incorrect Python syntax.
   - Must be fixed before the program can run.

2. ValueError
   - Occurs when the data type entered does not match the expected type.
   - Common when converting user input to int() or float().

3. try and except
   - Used to catch runtime errors.
   - Replaces technical error messages with user-friendly messages.

4. else Block
   - Runs only when no exception occurs.
   - Useful for separating successful execution from error handling.

5. Input Validation
   - Checking whether user input matches expected requirements.
   - Prevents programs from crashing due to invalid input.

6. Infinite Validation Loops
   - Repeatedly request input until the user provides valid data.
   - Common in real-world applications.

7. Function-Based Exception Handling
   - Encapsulates validation logic inside reusable functions.
   - Makes code cleaner and easier to maintain.

Key Takeaways:

- Syntax errors must be fixed before a program can run.
- Runtime errors can be handled with try-except blocks.
- ValueError is one of the most common exceptions when working with user input.
- The else block executes only when no exception occurs.
- while True loops can be used to repeatedly validate user input.
- Functions help make exception handling reusable and organized.
"""




#  syntax errors can not be negletecd by system until we fix them by finding them

print("#" * 20, "new section", "syntax_error", sep=",")
x = int(input("please entaer a valid intiger"))
print(f"x is {x}")


print("#" * 20, "new section", "value_error", sep=",")
# value_errors are those errors created by use for example when user is asked to enter an intiger value but user entered string or a float will raise a value error 
# to resolve value_errors we use try except to improve errors 
#  with try except method we can not remove error entirely we just replace tehnical error message with a user friendly message

try:
    value = float(input("enter a floated value"))
    print(f"floated value is {value}")
  
#  with except block we just replace techical error message with a user friendly message  
except ValueError:
    print(f"entered data is not a float value")
    
    
print("#" * 20, "new section", "name_error", sep=",")
# NameError are the errors caused by improper veriable asignment
try:
    x = int(input("enter the value of x"))
except ValueError:
    print("invalid input or dataformat mismatch")
else:
    print(f"x is {x}")
    
print("#" * 20, "new section", "infinite_loop_error_handling", sep=",")
# a beeter aproach to set up an infinite loop untill user give apropriate data it will ask same input again and again untill user guve right input

while True:
    try:
        ver = int(input("plz enter a valid integer"))
    except ValueError:
        print("please enter a number")
    else:
        break
print(f"the value of ver is {ver}")


# print("#" * 20, "new section", "function based", sep=",")

def main():
    age = get_int()
    print(f"age is {age}")
    
def get_int():
    while True:
        try:
            age = int(input("whats your age"))
        except ValueError:
            print("please enter any number")
            # if we replace pass with above print function we still catch error untill user ^rovide right input but dnt show them any warning or message 
        else:
            break
    return age

main()
