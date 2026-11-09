# graphics.py


"""
Topic: Loops, Functions, and Pattern Printing

Concepts Covered:

1. Repetitive Tasks
   - Performing the same action multiple times.
   - Reduces duplicate code.

2. for Loops
   - Execute a block of code a fixed number of times.
   - Commonly used with range().

3. range()
   - Generate a sequence of numbers.
   - Frequently used to control loop iterations.

4. The Underscore Variable (_)
   - Used when the loop variable itself is not needed.
   - Indicates that the value will be ignored.

5. Function-Based Design
   - Move repetitive logic into reusable functions.
   - Improves readability and maintainability.

6. Function Parameters
   - Pass values into functions to make them flexible.
   - Example: width, height, and size.

7. Vertical Pattern Printing
   - Print symbols in a column.
   - Demonstrates loops inside functions.

8. Horizontal Pattern Printing
   - Print symbols in a row.
   - Demonstrates string multiplication.

9. Nested Loops
   - One loop inside another loop.
   - Useful for grids, tables, and pattern generation.

10. Square Pattern Generation
    - Create a 3x3 and NxN square.
    - Combines loops and functions.

11. String Multiplication
    - Repeat characters using the * operator.
    - Example: "#" * 5

12. Multiple Solutions To The Same Problem
    - Compare different implementations.
    - Understand trade-offs between approaches.

Key Takeaways:

- Loops eliminate repetitive code.
- Functions make logic reusable.
- Parameters make functions more flexible.
- Nested loops are useful for two-dimensional patterns.
- String multiplication is a simple way to create repeated output.
- Many programming problems can be solved in multiple valid ways.
"""


print("#")
print("#")
print("#")
 
 
print("#"*20, "new section")
# same work can be done through 

for _ in range(3):
    print("#")
    
    

print("#"*20, "new section")
# now we will change inner implimention of a function 
print("we will print # sign verticaly ")

def main():
    print_column(3)
    
def print_column(height):
    for _ in range(height):
        # print("#")
        print("#\n" * height, end="")
        
main()

def print_column(width):
    for _ in range(width):
        print("#\n" * width)
        
        
print("#"*20, "new section")
# now we will change inner implimention of a function 


print("in this section we will print ? sign horizently through function ")
def man():
    print_row(3)
    
    
def print_row(width):
    print("?" * width)
    
man()


print("#"*20, "new section")
# now we will change inner implimention of a function 


print("in this section we will print # sign  through 3x3  ")

def seq():
    print_square(3)
    
def print_square(size):
    # for each row in square
    for i in range(size):
        # for each bloc/brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        print()

seq()

# alternative approach
print("#"*20, "new section")
def alternative_approach():
    print_altr(3)
        
def print_altr(size):
    for i in range(size):
        print("#" * size)
        
alternative_approach()