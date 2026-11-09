
"""
Topic: Conditional Statements

Concepts covered:
1. if
2.if-elif-else
3. if-else
4. Comparison operators
5. Logical operators (and, or)
6. Real-world examples
"""



# comparing two values 
print("#" *20, "simple compersion with only if statements")
x = 88
y = 98

if x > y:
    print(f"{x}is greater than {y}")
    
if x < y:
    print(f"{x} is less than {y}")
    
if x == y:
    print(f"{x} is equal to {y}")


# comapring values with if and elif statements

print("#" *20, "comparison with if and elif conditional statements")


if x > y:
    print(f"{x}is greater than {y}")
    
elif x < y:
    print(f"{x} is less than {y}")
    
elif x == y:
    print(f"{x} is equal to {y}")

# best structure
print("#" *20, "comaprison with if elif and else conditional statements")

if x > y:
    print(f"{x}is greater than {y}")
    
elif x < y:
    print(f"{x} is less than {y}")
    
else:
    print(f"{x} is equal to {y}")



# The OR operator returns True if at least one condition is True
print("#" * 20, "comapring with or either this one or that one")

x = int((input("enter any intiger")))
y = int(input("enter second integer"))

if x > y or x < y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")
    
    

a = int(input(" enater the value of a"))
b = int(input(" enater the value of b"))

if a != b:
    print(f"{a} is not equal to {b}")

else:
    print(f"{a} is equal to {b}")
    
    
# and operator retirns True only when both condition a and b are true
print("#" * 20, "in this section we will create a grades\n calculaor with if elif else and using and \n operator which means condition\n a nd b sould both be matched or true")

score = int(input("score:"))

if score >= 90 and score <= 100:
    print(f"student achieved A grade with a score of {score}")

elif score >= 80 and score < 90:
    print(f"student achieved B grade witha score of {score}")
elif score >= 70 and score < 80:
    print(f"student achieved c grade witha score of {score}")
elif score >= 60 and score < 70:
    print(f"student achieved D grade witha score of {score}")
else:
    print("better Luck Next Time")
    

# even or odd 

number = int(input("enter a number we will tell you weather its even or odd:"))
if number % 2 != 0:
    print (f"your number{number} is odd")
else:
    print(f"entered number{number} is even")
    
# same approach 

even_odd = int(input("enter a number we will tell you weather its even or odd:"))
if even_odd % 2 == 0:
    print (f"your number{even_odd} is even")
else:
    print(f"entered number{even_odd} is odd")
    
    
    
# modular version 

def main ():
    x = int(input(f"enter any number"))
    if is_even(x):
        print("even")
    else:
        print("odd")
        
def is_even(n):
    if n % 2== 0:
        return True
    else:
        return False
    
main()

