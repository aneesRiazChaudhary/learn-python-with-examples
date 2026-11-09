# intiger_data.py  


"""
Topic: Integer and Float Data Types

Concepts Covered:

1. User Input
   - Accept data from users using input().
   - Convert string input into numeric data types.

2. Integer Data Type (int)
   - Store whole numbers.
   - Perform arithmetic operations such as addition.

3. Float Data Type (float)
   - Store decimal numbers.
   - Useful for measurements, percentages, and calculations.

4. Type Conversion
   - Convert user input into integers using int().
   - Convert user input into decimal numbers using float().

5. Arithmetic Operations
   - Add numeric values together.
   - Display calculated results.

6. Rounding Numbers
   - Use round() to round decimal numbers.
   - Convert floats to the nearest whole number.

7. Number Formatting
   - Format large numbers using comma separators.
   - Improve readability of numeric output.

8. Floating Point Precision
   - Display a specific number of decimal places.
   - Format output using f-strings.

9. Formatted String Literals (f-strings)
   - Embed variables directly into strings.
   - Improve output readability.

10. Basic Function Usage
    - Create and call functions.
    - Reuse code through function definitions.

Key Takeaways:

- All user input is received as text by default.
- int() converts data into whole numbers.
- float() converts data into decimal numbers.
- round() simplifies decimal values.
- f-strings provide clean and readable output formatting.
- Numeric formatting improves the presentation of results.
- Functions help organize and reuse code.
"""


item_one = int(input("Please enter first value:"))
item_two = int(input("Please enter second value:"))
print(f"results: {item_one + item_two}")


#  float 
x = float(input("pleases enter a value:"))
y = round(x)
print(f"{x} rounds to: {y}")

# intiger seprator into killo,milion 

x = float(input("enter a floated value"))
y = float(input("enter a floated value"))

z = x+y
print(f"floated x+y results with comma sepration: {z:,}")


# after decimal two digits only 

x = float(input("enter a doted value"))

print(f"{x:.2f}")

#  functions

def hello ():
    print("hello")
    
name = input("what's your name")
hello()
print(name)