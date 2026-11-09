# code_to_be_tested.py


"""
Topic: Writing Testable Functions

Concepts Covered:

1. Function Definitions
   - Create reusable blocks of code using def.
   - Organise program logic into smaller components.

2. User Input
   - Accept numeric values using input().
   - Convert text input into integers.

3. Mathematical Functions
   - Create functions that perform calculations.
   - Return computed results.

4. Return Statements
   - Send values back to the caller.
   - Allow functions to be reused throughout a program.

5. Square Calculations
   - Calculate the square of a number.
   - Example: n * n

6. Cube Calculations
   - Calculate the cube of a number.
   - Example: n ** 3

7. Higher Powers
   - Raise values to larger exponents.
   - Example: n ** 4

8. Function Reusability
   - Reuse the same function with different inputs.
   - Avoid duplicated calculations.

9. Separation of Logic
   - Keep calculations separate from user input.
   - Makes programs easier to maintain.

10. Testable Code
    - Functions that return values are easier to verify.
    - Ideal candidates for automated testing.

Key Takeaways:

- Functions should perform a single responsibility.
- return allows functions to produce reusable results.
- Mathematical operations can be isolated inside functions.
- Small focused functions are easier to debug and test.
- Testable functions are the foundation of reliable software development.
"""


def main():
    x = int(input("please enter an intiger"))
    print(f"the square of x is {x}")
    
    
def squre(n):
    return n*n

def cube(n):
    return n**3 

def power_four(n):
    return n**4

#  if __name__ == "__main__"  by ading this line of code main will only be called in the imporitng and remaining functions can be called without implementing main 