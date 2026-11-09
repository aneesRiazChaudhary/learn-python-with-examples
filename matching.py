# matching.py

"""
Topic: Conditional Matching and Pattern Matching

Concepts Covered:

1. Conditional Statements
   - Use if, elif, and else to make decisions.
   - Execute different code based on different conditions.

2. Comparison Operators
   - Compare values to determine program flow.
   - Example: ==

3. Logical Operators
   - Combine multiple conditions using or.
   - Check whether any condition evaluates to True.

4. Multiple Condition Matching
   - Group related values under a single outcome.
   - Reduce repetitive code.

5. Decision Trees
   - Direct program execution based on user input.
   - Useful for menus, classifications, and categorization.

6. Pattern Matching (match-case)
   - A modern alternative to long if-elif chains.
   - Introduced in Python 3.10.

7. case Statements
   - Compare values against specific patterns.
   - Execute matching code blocks.

8. Default Case (_)
   - Acts like an else statement.
   - Handles unmatched values.

9. Multiple Value Matching
   - Match several values in a single case using |.
   - Reduces code duplication.

10. Code Readability
    - Pattern matching can make complex decision logic
      easier to understand and maintain.

Key Takeaways:

- if, elif, and else control decision-making.
- Logical operators help combine conditions.
- match-case provides a cleaner alternative for many comparisons.
- The underscore (_) acts as a default case.
- Multiple values can be handled within a single case.
- Pattern matching improves readability when many possible outcomes exist.
"""


name = input("whats your name")

if name == "saad" or name == "ahmer" or name == "ali" or name == "zain":
    print("chaudhary house")
    
elif name == "khizar":
    print("sultan house")
    
else:
    print("unknown family")
    
    
# same can be done with matching case where _ is used as same function of else 


name = input("enter your name ")

match name:
    case "shabeer":
        print("sultan house")
    
    case "zaheer":
        print("Dr House")
        
    case "abbass":
        print("advoacte house")
        
    case _:
        print("no house matched ")
        

# similiar aproach in some sort of pythonic way 

match name:
    case "ashfaq" | "naveed" | "anees":
        print("business class")
        
    case "ateeq" | "ahsan":
        print("Chauudhary_brothers")
        
    case _:
        print("not in list of our ppl")
        
    