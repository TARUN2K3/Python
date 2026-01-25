#Special_Character_in_regular_expression
'''
    1. [...] --> Contain set of all possible character
    2. [^..] --> All charcter except in bracket
    3. . --> Any character except new line
    4. ^ --> Beginning of the string
    5. $ --> End of the string
    6. R|S --> R or S'''

# Lowercase
import re
pattern = r'[a-z]+'
print(re.match(pattern,'board'))

#Capitalized
pattern_1 = r'[A-Z][a-z]*'
print(re.match(pattern_1,'Board'))

#First_name and Last_name
pattern_2 = r'[A-Z][a-z]+ [A-Z][a-z]*'
print(re.match(pattern_2,'Tarun Sharma'))

#Varibale_name_pattern
pattern_3 = r'[A-Za-z_][A-Za-z0-9_]*'
print(re.match(pattern_3,'_Pattern_3'))

#Time in 24 Hours Format
pattern_4 = r'[012][0-9]:[0-5][0-9]'
print(re.match(pattern_4,'11:02'))

#Domain name pattern
pattern_5 = r'[a-zA-Z0-9]+\.(org|com|in)$'
print(re.match(pattern_5,'tarunsharma2k3.com'))

#checking site starting with 'https'
pattern_6 = r'^(https.)[a-zA-Z0-9]+'
print(re.match(pattern_6,'https.tarun23'))