# csv_pyt_module.py
"""
Topic: CSV Module

Concepts Covered:

1. The csv Module
   - Python's built-in module for working with CSV files.
   - Simplifies reading and writing tabular data.

2. csv.reader()
   - Read CSV files row by row.
   - Convert each row into individual values.

3. Variable Unpacking
   - Extract values directly from CSV rows.
   - Example:
       name, home = row

4. Building Lists of Dictionaries
   - Convert CSV records into dictionaries.
   - Create structured datasets.

5. Sorting Records
   - Use sorted() to organize data.
   - Display records in a meaningful order.

6. Lambda Functions
   - Create small anonymous functions.
   - Commonly used for sorting operations.

7. Sorting With key=
   - Specify which field controls sorting.
   - Example:
       key=lambda student: student["name"]

8. csv.DictReader()
   - Read CSV files using column names.
   - Access values through dictionary keys.

9. Working With Headers
   - Use column names instead of index positions.
   - Makes code more readable.

10. csv.writer()
    - Write rows to CSV files.
    - Store data in tabular format.

11. writer.writerow()
    - Add new records to a CSV file.
    - Save lists as CSV rows.

12. csv.DictWriter()
    - Write dictionary data directly to CSV files.
    - Match values using field names.

13. fieldnames
    - Define column names for CSV output.
    - Ensure data is stored consistently.

14. Appending Data
    - Use append mode ("a") to preserve existing records.
    - Add new rows without overwriting data.

Key Takeaways:

- The csv module is the preferred way to work with CSV files.
- csv.reader() processes rows as sequences.
- csv.DictReader() provides dictionary-based access.
- csv.writer() creates CSV rows from lists.
- csv.DictWriter() creates CSV rows from dictionaries.
- Lambda functions simplify custom sorting.
- CSV files are widely used for data storage and exchange.
"""

import csv 

students = []

with open("sample.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "home":home})
        
for student in sorted(students, key= lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")
    
    
stars = []

with open("sample.csv") as stars_data:
    reader = csv.DictReader(stars_data)
    for row in reader:
        stars.append({"name": row["name"], "state":row["state"]})
        
for star in sorted(stars, key=lambda star: star["name"]):
    print(f"{star['name']} is from {star['state']}")
    
    
print("#" *20, "now we will wite a csv and store data in in with python csv module")


# with open("data.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name_person","stae_country"])

name_person = input("what is your name?")
stae_country = input("your country?")
with open("data.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name_person,stae_country])
    
    
hero_name = input("hero name")
movie_name = input("movie name")
with open("data.csv", "a") as heros_file:
    writer = csv.DictWriter(heros_file, fieldnames=["name","home"])
    writer.writerow({"name":hero_name,"home":movie_name})

    