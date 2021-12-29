import re

vowelsMatch=re.compile(r'[aeiouAEIOU]')
list=vowelsMatch.findall("I am the greatest of all time")

dict={}
for item in list:
    dict.setdefault(item,0)
    dict[item]=dict[item]+1
print(dict)