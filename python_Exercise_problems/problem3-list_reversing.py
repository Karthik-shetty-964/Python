n=int(input("Enter the number of items of the list"))
list=[]
for i in range(n):
    j=input()
    list.append(j)

def built_in_func(list):
    list.reverse()
    return list

def slicing_method(list):
     list2=list[::-1]
     return list2


def manual_reversing(list):
    for i in range(int(n/2)):
        temp=list[i]
        list[i]=list[n-1-i]
        list[n-1-i]=temp

    return list

print(built_in_func(list))
# print(slicing_method(list))
# print(manual_reversing(list))
# print(list[n-1])