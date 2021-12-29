# practice project
# ist =["karthik","shreya","keerthan","apeksha","jithesh"]
# str=""
# for item in list:
#     if list.index(item)==len(list)-1:
#         str+=" and "
#         str+=item
#         break   
#     str+=item
#     str+=", "
# print(str)

# Dictionaries

# dict={'apples':5,'cups':2,'poonki':'yes'}
# print(dict.get('poonki'))
# dict['oranges']=56
# if 'banana' not in dict:
#     dict['banana']=10
# print(dict)
# dict.setdefault('poonki','no')
# print(dict)

# Count the number of occurances of a character in a string
import pprint
message="jdfhkdf kjfdk kajfdhh ihj fier kfkdj iajfidj hjkfghri ihgirjgl ll djkf"
count={}

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(list)
