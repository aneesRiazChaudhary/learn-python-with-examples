# dictionary_loops.py

"""
Topic: Dictionaries and Dictionary Loops

1. Access values by key
2. Print entire dictionary
3. Loop through keys
4. Loop through values using keys
5. Print key-value pairs
6. View dictionary keys
7. Access keys by index
8. List of dictionaries
9. Loop through a list of dictionaries

Key Takeaways:
- Dictionaries store data as key-value pairs.
- Keys are used to access corresponding values.
- By default, looping through a dictionary returns keys.
- Values can be accessed through their keys.
- Dictionaries can be combined with lists to represent structured data.
- A list of dictionaries is commonly used in real-world datasets, APIs, and JSON files.
"""


print("###"*10)
print("print any value of the dictionry through any key")
students_dict = {"taha":"phy",
                 "moosa":"king_maker",
                 "zain":"king"}
print(students_dict["moosa"])

print("###"*10)
print("print all keys and values")
print(students_dict)


# now we will print all keys of the dict 
print("###"*10)
print("all keys of the dictionary not values")

for keys in students_dict:
    print(keys)
    

print("###"*10)
print("all values from dict through their keys")

for k in students_dict:
    print(students_dict[k])
    
# key value pairs
print("###"*10)
print("all key value pairs")   

for key in students_dict:
    print(key, students_dict[key], sep=", ")
    
# now we will print key on desired postion or index
print("###"*10)
print("list of keys")

print(students_dict.keys())

print("###"*10)
print("print keys at desired index")

ky_3rd = list(students_dict.keys())[2]
print(ky_3rd)



print("###"*10)
print("multiple data associated with same keys")
# when we have multiple data associated with keys 

# for example if we have a table or dataset like this 
#      name      House        sigil
# 0    saad     chaudhary      sword
# 1    moosa    elite          wear wolf
# 2    ali      king           crown

# a list of dictionaries with same keys and unique values 

data = [
    {"name":"saad", "house":"chaudhary", "sigil": "sword"},
    {"name":"moosa", "house":"elite", "sigil": "wear wolf"},
    {"name":"ali", "house":"king", "sigil": "crown"},
    {"name":"ahmer", "house":"chaudhary", "sigil": None}
]

for item in data:
    print(item["name"], item["house"], item["sigil"], sep=", ")