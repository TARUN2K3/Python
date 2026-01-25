#Escape_Sequence_in_regular_expression
'''Escape sequence start with the backslash(\) that represent common character class such as digits, non-digits, alphanumeric, whitespace and position within the string
    1. \d --> Digits[0-9]
    2. \D --> except digit[a-zA-Z+-....]
    3. \w --> Alphanumeric[a-zA-Z0-9] and underscore
    4. \W --> Non-alphanumeric and underscore
    5. \s --> whitespaces
    6. \S --> Non-Whitespaces
    7. \A --> start of string anchor
    8. \Z --> End of string anchor '''

#Pattern of date format dd/mm/yyyy
import re
pattern = r'\d{2}/\d{2}/\d{4}'
print(re.match(pattern,'01/01/2026'))

#pattern of password: alphanumeric and underscore, minimum 8 character
pattern_1 = r'[\w_]{8}'
print(re.match(pattern_1,'abc_2323'))

#Pattern of simplified E-mail
pattern_2 = r'\A\w+@gmail\.(com|org|in)\Z'
print(re.match(pattern_2,"tarunsharma2k3@gmail.com"))
