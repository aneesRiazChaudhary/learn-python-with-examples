# code_tester.py
# we will create a new py file and test its functionality through our code_tester.py

"""
Topic: Testing Python Code

Concepts Covered:

1. Importing Functions
   - Import functions from another Python file.
   - Test functionality without rewriting code.

2. Code Reusability
   - Separate application logic from testing logic.
   - Organize projects into multiple files.

3. Manual Testing
   - Compare expected results with actual results.
   - Identify incorrect calculations.

4. Test Functions
   - Create dedicated functions for testing.
   - Keep tests separate from application code.

5. Testing Expected Outputs
   - Verify that functions return correct values.
   - Compare actual results against known answers.

6. Assertion Testing

   assert condition

   - Ensures a condition evaluates to True.
   - Raises an AssertionError when a test fails.

7. Automated Testing
   - Run multiple tests quickly and consistently.
   - Detect mistakes after changing code.

8. AssertionError
   - Triggered when an assertion fails.
   - Indicates unexpected behaviour.

9. try-except With Assertions
   - Catch failed assertions gracefully.
   - Display custom error messages.

10. Program Entry Points

    if __name__ == "__main__":

    - Execute code only when the file is run directly.
    - Prevent automatic execution when imported.

11. Test Organization
    - Separate tests by functionality.
    - Example: square tests, cube tests, power tests.

Key Takeaways:

- Testing helps verify program correctness.
- Assertions simplify validation of expected results.
- Automated tests save time and improve reliability.
- Failed assertions indicate possible bugs.
- Separating code and tests improves maintainability.
- Testing is an essential part of professional software development.
"""





from code_to_be_tested import squre, cube, power_four

def main():
    test_square()
    test_cube()
    test_power()

def test_square():
    if squre(2) != 4:
        print("2 square is not equal to 4 maeans problem in square function")
        
    if squre(3) !=9:
        print("3 square is not equal to 9 maeans problem in square function")
        
print("#" *20, "instead of ifelse testing now we will use assert for testing")        


def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27

print("#" *20, "now we will add try except with assertion ")        

def test_power():
    try:
        assert power_four(2) == 16
    except AssertionError:
        print("problem in power function")
    try:
        assert power_four(3) == 81
    except AssertionError:
        print("prblem in function because 3 power 4 must be 81")

if __name__ == "__main__":
    main()