#Regular_Expression
''' Regular Expression is the pattern describing set of the string usign for the pattern matching 
    Using:-
    1.Text processing
    2.Data Validation
    3.Information Extraction'''
# 're' library in python contains built in regex function must be imported by "import re"

'''Key function
    1. compile(pattern,flags=0) --> Compile a pattern in to regex function for reuse
    2. match(pattern,string,flags=0) --> checks if pattern matching in the start of the string
    3. fullmatch(pattern,string,,flag=0) --> check is entire string is matches the pattern
    4. search(pattern,string,flag=0) --> search for first occurence of the pattern anywhere in the string
    5. finall(pattern, string, flag=0) --> Return all non-overlapping matches of pattern in the string as a list
    6. split(pattern, string, maxsplit=0, flags=0) --> split string by occurence of pattern'''

import re
string = "python is my first language"
pattern = "my"
result = re.match(pattern,string)
print(result) # This code will not work because match function will check only starting of the string

string_2 = "my first language is python"
pattern_2 = "my"
result_2 = re.match(pattern_2,string_2)
print(result_2)
print(result_2.group())


string_3 = "python"
pattern_3 = "python"
result_3 = re.fullmatch(pattern_3,string_3)
print(result_3)
print(result_3.group())

string_4 = "python is my fisrt language"
pattern_4 = "my"
result_4 = re.search(pattern_4,string_4)
print(result_4.group())

string_5 = "python my is my fisrt language my"
pattern_5 = "my"
result_5 = re.findall(pattern_5,string_5)
print(result_5)

string_6 = "python my is my fisrt language my"
pattern_6 = "my"
result_6 = re.split(pattern_6,string_6)
print(result_6)







