# List comprehension
# Write a program to create a list which has multiple of 3
# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)
#
# ls2=[i for i in range(100) if i%3==0 ]
# print(ls2)

# 2-->Dictionary comprehension
# dict1={0:item0 , 1:item1 ......}

# dict1={i:f"item{i}" for i in range(10)}
# print(dict1)
#
# #We can even interchange the key and values
# dict1={value:key for key,value in dict1.items()}
# print(dict1)

#3-->Generator comprehensions
# mulOf3=(i for i in range(10) if i%3==0)
# print(mulOf3.__next__())
# print(mulOf3.__next__())
# print(mulOf3.__next__())
#
# for i in mulOf3:
#     print(i)
