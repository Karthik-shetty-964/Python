import json

# json.loads()-->It is used to convert a string into json object in the form of key and values

# string='{"name":"karthik","age":19,"car":"BMW"}'
# print(string)
# js_data=json.loads(string)
# print(js_data['car'])
# print(js_data['name'])
# print(js_data['age'])

"""
json.dumps()-->It is used to convert any python variables in java script variables
               
"""
# data={
#     "name": "karthik",
#     "cars": ["BMW","Audi","Porsche"],
#     "phones":("iphone","samsung","Realme"),
#     "isbad":False
# }
#
# js_data=json.dumps(data,sort_keys=True)
# print(js_data)


"""
json.load()-->It is used to convert a file object into a json object
"""
# f=open("karthik.txt")
#
# js_data=json.load(f)
#
# for i in js_data:
#     print(i)