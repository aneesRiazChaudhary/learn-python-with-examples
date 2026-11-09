# loops.py

"""
Topic: Loops and Repetition

Concepts Covered:

1. while Loops
   - Execute code repeatedly while a condition remains True.
   - Useful when the number of repetitions is unknown.

2. Loop Counters
   - Control the number of loop iterations.
   - Increase or decrease values during execution.

3. Augmented Assignment
   - Use += and -= operators.
   - Simplifies counter updates.

4. for Loops
   - Iterate over sequences or ranges.
   - Ideal when the number of repetitions is known.

5. range() Function
   - Generate a sequence of numbers.
   - Frequently used with for loops.

6. Loop Variables
   - Store the current item or value during iteration.
   - Often named i for counting purposes.

7. Underscore Variable (_)
   - Used when the loop variable is not needed.
   - Common for simple repetition tasks.

8. String Repetition
   - Repeat strings using the * operator.
   - Alternative approach for simple repeated output.

9. Infinite Loops
   - Loops that continue until explicitly stopped.
   - Often used for input validation.

10. break Statement
    - Immediately exits a loop.
    - Used when a desired condition is met.

11. continue Statement
    - Skips the current iteration.
    - Continues with the next loop cycle.

12. Input Validation
    - Keep requesting input until valid data is provided.
    - Improves program reliability.

13. Combining Loops and Functions
    - Use loops inside functions.
    - Create reusable and organized code.

14. Returning Values From Functions
    - Use return to send validated data back.
    - Separate user input logic from processing logic.

Key Takeaways:

- Loops automate repetitive tasks.
- while loops run based on conditions.
- for loops run over ranges or collections.
- break exits a loop early.
- continue skips the current iteration.
- Input validation is commonly implemented using loops.
- Functions and loops work together to build reliable programs.
"""

i = 3
while i !=0:
    
    print("hello")
    i = i-1
    
# different logic same results 

i = 1
while i <= 3:
    print("how are you")
    # i = i + 1
    #  or
    i += 1
    
# another similair approach 

i = 0

while i < 3:
    print("where are you from?")
    i += 1
     

#  for loop on list 

for i in [0,1,5]:
    print("what is your age?")
    
# similar functnionality 

for i in range(3):
    print("what do you like?")
    
# instead of veriable i we can use _ to create a veriable which is not used but necessory for loop structre 

for _ in range(3):
    print("are you free today?")
    
# similar work can be done without any loop

print("are you ok?\n" * 3, end="")


# an infinite loop 

while True:
    n = int(input("enter any numer"))
    if n <=0:
        # print("please enter a valid number")
        continue
    else:
        break
    
    
# similiar way 

while True:
    n = int(input("enter a number"))
    if n > 0:
        break
    
for _ in range(n):
    
    print("today is a good day")
   
   
   
   
# functions and loops 

def main():
    number = get_number()
    hello(number) 
    
    
def get_number():
    while True:
        n = int(input("enter n "))
        if n > 0:
            break
        
    return n
    
def hello(n):
    for _ in range(n):
        print("hello,world")
        
main()