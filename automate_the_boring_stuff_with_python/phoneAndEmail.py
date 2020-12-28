#! python3
#phoneAndEmail finds phone number and email addresses on the clipboard

import pyperclip, re, sys
"""
phoneregex = re.compile(r'\d{3}.\d{3}.\d{4}')
dat_regex = re.compile(r'https?://www\.?\w+\..com|.fr')
dat_email = re.compile(r'([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z0-9-.]+)')
#phoneregex = re.compile(r'\d\d\d\s|\d\d\d\w')
matches = dat_email.search(sys.argv[1])
"""
phoneRegex = re.compile(r'''( 
(\d{3}|\(\d{3}\))?                # area code
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

"""emailRegex = re.compile(r'''([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+(.com|.fr)
)''', re.VERBOSE)
"""

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)

text = pyperclip.paste()
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied')
    print('\n'.join(matches))
else:
    print('No phone or number find')

#print(pyperclip.paste())
