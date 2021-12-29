pebbles=[1,2,3,4,4,3,2,1]
# pebbles=[1,2,3,4,4,4,3,2,1,2]


list=[]
counts=0

for item in pebbles:
    counts=pebbles.count(item)
    list.append(counts)


key=list[0]
for i in list:
    if(i!=key):
        print("false")
        exit()

print("true")
