#  functions.py

"""
Topic: Functions

Concepts Covered:

1. Creating Functions
   - Define reusable blocks of code using def.
   - Execute code only when the function is called.

2. Calling Functions
   - Run a function by using its name followed by parentheses.

3. Function Parameters
   - Pass data into a function.
   - Parameters allow functions to work with different values.

4. Function Arguments
   - Values supplied when calling a function.
   - Arguments are assigned to function parameters.

5. Default Parameters
   - Assign default values inside function definitions.
   - Functions can run even when no argument is provided.

6. Organizing Programs With Functions
   - Break large programs into smaller reusable components.
   - Improve readability and maintainability.

7. The main() Function
   - Acts as the starting point for program execution.
   - Helps organize program flow.

8. Returning Values
   - Use the return statement to send data back from a function.
   - Returned values can be stored, printed, or reused.

9. Separating Tasks Into Functions
   - One function can gather input.
   - Another function can process the data.
   - Improves code reusability.

10. Building Mathematical Functions
    - Functions can perform calculations and return results.
    - Example: calculating the square of a number.

Key Takeaways:

- Functions help eliminate repetitive code.
- Parameters make functions flexible and reusable.
- Default parameters provide fallback values.
- Return statements allow functions to produce results.
- main() helps structure larger programs.
- Well-designed functions make programs easier to read, test, and maintain.
"""


def hello ():
    print("Hello,")
    
name = input("what's your name").title()
hello()
print(name)

# adding parameter to a function 

def hello (to):
    print("Hello,", to)
    
name = input("what's your name").title()
hello(name)
# print(name)

# parameters can be assign with in function breakets at the same time 
def hello (to = "world"):
    print("Hello,", to)
 
hello()   
name = input("what's your name").title()
hello(name)


def main():
    x = int(input("enter any intiger"))
    print(f"the square of {x} is {x**2}")
    
main()

# same funtion as above 

def man():
    x = float(input("enter a floated value"))
    print("x spuare is", square(x))
    
def square(n):
    # return n **2
    return n * n

man()