import re

string ="""The module defines several functions and constants to work with RegEx. 
         module is composed of five functio654561321 6551651 522465421 6854654448ns known as:findall: It finds all searc
         hes for matches and prints resultant in the form of a list.search: It works the sam
         e as a findall, but the resultant is a matched word with a word of our choice"""

# patt=re.compile(r'\d4+')
#
# macthes=patt.finditer(string)
# for match in macthes:
#     print(match)


# test:To return the phone numbers starting with +91

Ph_Numbers="+91 9964300358 , +91 9880414983, +91 8152990056, +6595+62+65 . +5+5+9595+9k, +5+98*595986546484,, 65689865467986, +91 9844454583"

patt=re.compile(r'.+91 \d{10}')
matches=patt.finditer(Ph_Numbers)
for match in matches:
    print(match)