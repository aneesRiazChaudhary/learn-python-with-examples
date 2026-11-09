# file_input_output.py  
"""
Topic: File Handling

Concepts Covered:

1. Working With Lists
   - Collect multiple values using append().
   - Store user input in a list.

2. Temporary vs Persistent Data
   - Variables and lists exist only while the program is running.
   - Data is lost when the program stops unless it is saved to a file.

3. Creating Files
   - Use open() with write mode ("w").
   - Create a new file and store data in it.

4. Writing Data To Files
   - Use write() to save information.
   - Store user-provided data for future use.

5. File Modes
   - "w" (Write Mode)
     Creates a new file or overwrites an existing file.

   - "a" (Append Mode)
     Adds new data to the end of an existing file.

   - "r" (Read Mode)
     Opens a file for reading.

6. Closing Files
   - Use close() to release file resources.
   - Ensure data is properly saved.

7. Using The with Statement
   - Automatically handles file closing.
   - Preferred and safer approach for file operations.

8. Reading Files
   - Read data from existing files.
   - Access information stored in previous program runs.

9. Reading Lines From A File
   - Use readlines().
   - Store file contents inside a list.

10. Iterating Through File Contents
    - Loop through file lines one by one.
    - Process large files efficiently.

11. Removing Extra Whitespace
    - Use rstrip().
    - Remove new line characters from output.

12. Building Lists From Files
    - Read file data into a list.
    - Perform operations such as sorting.

13. Sorting File Data
    - Sort entries alphabetically.
    - Display organized information.

Key Takeaways:

- Files allow programs to store data permanently.
- Data written to a file remains available after the program ends.
- Write mode overwrites data while append mode preserves existing data.
- The with statement is the recommended way to work with files.
- File contents can be read, processed, stored in lists, and sorted.
- File handling is a fundamental skill used in data processing, automation, and software development.
"""


names = []



for _ in range(3):
    
    names.append(input("what is your name?"))
    
for name in sorted(names):
    print(f"hello, {name}")

# all the program progress lost when we close our code editer all the data created will also be lost until we re run a program 

# now we will write or create our first file 


profession = input("your source of income")

file = open("professions.txt", "w")
file.write(profession)
file.close()


# "w" in file creating function will re write 
# every time we run the creating function we 
# will repace it with "a" which will append the 
# information in the file 

country = input("your country name?")
countries_file = open("countries.txt", "a")
countries_file.write(f"{country}\n")
countries_file.close()


# a beeter approach is to use with keyword 
uni = input("share your uni name ")
with open("universties.txt", "a") as university_file:
    university_file.write(f"{uni}\n")
    university_file.close()
    
    
# now we will use an existing fole to read 
# reading a file


with open("universties.txt", "r") as uni_file:
    lines = uni_file.readlines()
    
for line in lines:
    print("i am from ", line.rstrip())
    
# in the above code snipt we first read lines from the 
# file then itreate over them . in next section we will 
# do the same work in single code logic reading and iterating

with open("universties.txt", "r") as uni_file:
    for line in uni_file:
        print("hello", line.rstrip())
        
        
# now we will append new data in the list and then print

unies = []
with open("universties.txt") as unies_files:
    for line in unies_files:
        unies.append(line.rstrip())
        
for uni in sorted(unies):
    print(f"greetings,{uni}")
    
# we can sort file directly without inilizing a list
# in next section we will directly sort file data

with open("universties.txt") as top_uni:
    for line in sorted(top_uni):
        print("toppers,", line.rstrip())