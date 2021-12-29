import re

emailExtract=re.compile(r'[A-Za-z0-9]+@[a-zA-Z]+\.[a-z]+|[0-9]{10}')
# mo=emailExtract.search('''Karthik's email address- karthiksshetty111@gmail.com
#                             Apeksha's email address-apekshashetty21@gmail.com
#                             google email-googleworld@ac.in 9964300358
#                             +91 9839483939''')
mo=emailExtract.findall('''Karthik's email address- karthiksshetty111@gmail.com
                            Apeksha's email address-apekshashetty21@gmail.com
                            google email-googleworld@ac.in 9964300358
                            +919839483939''')
# print(mo.group(1))
# print(mo.group())
print(mo)