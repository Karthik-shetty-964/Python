import re,pyperclip
import clipboard
clipboard.copy("")
phoneRegex=re.compile(r'''(
                     (\d{3}|\(\d{3}\))?                 #area code
                     (\s|-|\.)?                         #separator
                     (\d{3})                            #first 3 digits
                     (\s|-|\.)?                         #separator
                     (\d{4})                            #next three digits
                     (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
                     )''',re.VERBOSE)

emailRegex=re.compile(r'''(
                        [a-zA-Z0-9._%+-]+ 
                        @
                        [a-zA-Z0-9.-]+
                        \.[a-zA-Z]{2,4}
                        )''',re.VERBOSE)


text=str(pyperclip.paste())

matches=[]
for groups in phoneRegex.findall(text):
    phoneNum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phoneNum +='x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


for groups in emailRegex.findall(text):
    matches.append(groups[0])

#copy the results
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copies to clipboard: %s' % matches)
    print('\n'.join(matches))
else:
    print('no phone numbers or email address found.')