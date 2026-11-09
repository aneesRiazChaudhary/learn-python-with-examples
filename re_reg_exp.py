# re_reg_exp.py

"""
Topic: Regular Expressions (Regex)

Concepts Covered:

1. The re Module
   - Python's built-in module for pattern matching.
   - Used for searching, validating, and extracting text.

2. Pattern Matching
   - Check whether text follows a specific format.
   - Commonly used for validation.

3. re.search()
   - Searches a string for a matching pattern.
   - Returns a match object if found.

4. Special Regex Characters

   .       Any character except a newline
   *       Zero or more repetitions
   +       One or more repetitions
   ?       Zero or one repetition
   {m}     Exactly m repetitions
   {m,n}   Between m and n repetitions

5. Anchors

   ^       Start of a string
   $       End of a string

   These help ensure the entire string follows a pattern.

6. Character Sets

   [abc]       Match a, b, or c
   [a-z]       Match lowercase letters
   [A-Z]       Match uppercase letters
   [0-9]       Match digits
   [^abc]      Match anything except a, b, or c

7. Escaping Special Characters

   \.          Match a literal dot (.)
   \w          Match letters, numbers, and underscores

8. Raw Strings

   r"pattern"

   Raw strings prevent Python from treating backslashes
   as escape characters.

9. Email Validation

   - Verify the presence of @
   - Verify domain names
   - Restrict allowed formats
   - Prevent invalid patterns

10. Optional Groups

    (?...)

    Use ? to make parts of a pattern optional.

11. Case Insensitive Matching

    re.IGNORECASE

    Allows matching regardless of letter casing.

12. Input Validation

    - Validate user input before processing.
    - Reduce formatting errors and bad data.

Key Takeaways:

- Regular expressions are powerful tools for text validation.
- Regex patterns can search, validate, and filter text.
- Anchors help validate complete strings.
- Character classes define accepted characters.
- Raw strings make regex easier to write and read.
- Regex is commonly used for email, username, URL, and password validation.
"""



# validation with re

#  . any charcter except a new line
#  * 0 or more repetations
#  + 1 or more repetations
#  ? 0 or 1 repetations
# {m} m repetations
#  {m,n} m-n repetations
#  re.search(pattern, string,flags)
#  ^ match start of the string
#  $ match end of the string


import re 


email = input("enter your email").strip()

if re.search("@", email):
    print("valid")
else:
    print("invalid email")
    

#  ".+@.+" means one or more cahr befre and after @
ur_mail = input("enter ur email")
if re.search(".+@.+",ur_mail):
    print("valid")
else:
    print ("invalid")
    
# similiar approach where we will replce .+   with  ..*

my_email = input("what is my email")
# this will vilidate a char before @ and a char after @ which means zero  or more cahr then@Then zero or more char
if re.search("..*@..*", my_email):
    print("valid email")
    
else:
    print("invalid")
    
    
# now we will validate only emails that contain edu at end
sadi_mail = input("sdi mail")
#  this will vilidate a char bfore @ and a char after @ and it must include edu
if re.search(r".+@.+\.edu", sadi_mail):
    print("valid")
else:
    print("invalid")
    
# corectinting seena  @  google. org  study with aditional carot and $ signs 

email_id = input("your id ")

if re.search(r"^.+@.+\.org$", email_id):
    print("format align")
else:
    print("invalid format")


# now we will make a restriction that in email we need one @ if it apears more than once in a single imail id it will be invalid email 

# [^@] means any thing any number or char it could be but will not be @ 

sign_in = input("enter ur sign in ").strip()

if re.search(r"^[^@]+[^@]+\.health$", sign_in):
    print("format align")
else:
    print("email@sad.health")
    
#  [a-zA-z0-9_] means incliding any char from a to z in both uper case and lower case and from zero to 9 and _ any number if we use a carot symbol in the same square bracet it means excluding all these
#  this will allow chars@chars.domin
login = input("enter your loin").strip().lower()

if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9_]+\.domain$", login):
    print("valid login")
    
else:
    print("invalid login")
    
# "^\w+@\w+\.co" now instead of [a-zA-Z0-9_] we will use r"^\w+@\w+\" which means words before and after @
# lower function will convert all capitals to lower casing if word seq as we ysed in our damain name 
signIn = input("enter ur signIn").strip()

# if re.search(r"^\w+@\w+\.CAP_Lower$", signIn.lower()): 
#  we can replace above line as 
if re.search(r"^\w+@\w+\.CAP_Lower$", signIn,re.IGNORECASE):
    print("valid signin")
else:
    print("invalid signin")
    
# ? means a seq can be present in or may be not 0 or 1 time 
# (\w+\.)? means format can be apear or may be not optional

id_adress = input("enter your adress").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.domain_name$", id_adress.lower()):
    print("validated")
else:
    print("invalid ")