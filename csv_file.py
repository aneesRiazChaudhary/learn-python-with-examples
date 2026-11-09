# csv_file.py


"""
Topic: CSV Files and Data Processing

Concepts Covered:

1. CSV Files
   - CSV stands for Comma-Separated Values.
   - Used to store tabular data in a text format.

2. Reading CSV Files
   - Open and read data from existing CSV files.
   - Process file contents line by line.

3. Splitting Data
   - Use split(",") to separate values.
   - Convert a CSV row into individual columns.

4. Removing Extra Characters
   - Use rstrip() to remove trailing newlines.
   - Produce cleaner output.

5. Variable Unpacking
   - Assign multiple values from a CSV row.
   - Example:
       name, country = line.split(",")

6. Working With Lists
   - Store processed CSV data in lists.
   - Build collections for later analysis.

7. Sorting Data
   - Use sorted() to arrange records alphabetically.
   - Improve data presentation.

8. Creating Dictionaries From CSV Data
   - Convert CSV rows into structured dictionary objects.
   - Associate field names with values.

9. Lists of Dictionaries
   - Store multiple records using dictionaries.
   - Create simple dataset structures.

10. Custom Sorting
    - Use the key parameter with sorted().
    - Define custom sorting behaviour.

11. Functions With Sorting
    - Create helper functions for sorting criteria.
    - Improve code readability and reusability.

12. Structured Data Processing
    - Transform raw CSV text into organized Python objects.
    - Prepare data for analysis and reporting.

Key Takeaways:

- CSV files are commonly used to store tabular data.
- split(",") separates CSV columns into values.
- Lists help store multiple records.
- Dictionaries create meaningful field-value relationships.
- sorted() can organize records alphabetically.
- The key parameter allows custom sorting rules.
- CSV processing is an important foundation for data analysis.
"""

print("in this section we used a two column\n csv data where values are seprated by comma")
with open("sample.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        
  
print("#" *20, "in this section we will give the name to\n all values using same split function") 
with open("sample.csv") as data:
    for line in data:
        name, countries = line.rstrip().split(",") 
        print(f"{name} is from {countries}")
    

print("#" *20, "now we will sort data")

students = []

with open("sample.csv") as df:
    for line in df:
        student_name, student_country = line.rstrip().split(",")
        students.append(f"{student_name} is a business class citizen of  {student_country}") 
        
for i in sorted(students):
    print(i)
    
    
print("#" *20, "now we will create a dictionry from two column data then sort it")

founders = []

with open("sample.csv") as founding_data:
    for line in founding_data:
        citizen, citizenship = line.rstrip().split(",")
        founder= {}
        founder["citizen"] =  citizen
        founder["citizenship"] =  citizenship
        founders.append(founder)

for i in founders:
    print(f"{i['citizen']} is the king of {i['citizenship']}")
    

print("#" *20, "creating dictionry sort values with key")


presidents = []
with open("sample.csv") as data_frame:
    for line in data_frame:
        person , country_state = line.rstrip().split(",")
        president = {"person":person, "country_state":country_state}
        presidents.append(president)
        
def get_person(president):
    return president["person"]

for president in sorted(presidents, key=get_person, reverse=True):
    print(f"{president['person']} is the head of {president['country_state']}")
        
         