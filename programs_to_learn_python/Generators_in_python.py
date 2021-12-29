"""
Iterable --> __iter__() , __getitem__()
Iterator --> __next__()
Iteration --> It is a process of iteratiing
"""

# k="Karthik"
# g=k.__iter__()
# # print(g.__next__())
# # print(g.__next__())
# # print(g.__next__())
#
# for i in g:
#     print(i)

"""
Generators --> These are same as iterators ,these iterates only oncers..ex:-range() ,yield
yield --> It is same as return fucntion ,but this returns a generator which can be accessed using for loops or __next__() function
"""
def gen(n):
    for i in range(n):
        yield i

g=gen(30)
# for i in g:
#     print(i)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())