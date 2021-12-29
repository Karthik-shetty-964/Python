n1=int(input("Enter the size of the first array"))
arr1=[]
print("Enter the elements fot the first array")
for i in range(n1):
    arr1.append(int(input()))

n1=int(input("Enter the size of the second array"))
arr2=[]
print("Enter the elements fot the second array")
for i in range(n1):
    arr2.append(int(input()))

n1=int(input("Enter the size of the third array"))
arr3=[]
print("Enter the elements fot the third array")
for i in range(n1):
    arr3.append(int(input()))

arr=arr1+arr2+arr3
arr.sort()
print(arr)