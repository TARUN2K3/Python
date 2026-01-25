#Quantifiers_in_regular_expression

'''Quantifiers that allows quantity of character or group repetitions in pattern
    1. + --> 1 or more repetitions
    2. * --> 0 or more repetitions
    3. ? --> 0 or 1 repetition only
    4. {m} --> matches excatly m number of repetition
    5. {m,n} --> matches at least m or at most n repetiton'''

'''Grouping and Character set
    () --> whole group
    [] --> any one character inside'''

import re
print(re.fullmatch('(ab)*','abababab'))
print(re.fullmatch('(ab)?','ab'))
print(re.fullmatch('(ab)+','abaaaab'))
print(re.fullmatch('[ab]+','abaaaab'))
print(re.fullmatch('[ab]{4}','abab'))
print(re.fullmatch('[ab]{1,4}','abab'))
