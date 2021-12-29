N=int(input("Enter the total number of candies"))
K=int(input("Enter the no. candies that should have same special value"))

arr=[]
print("Enter the special values of all the candies")
for i in range(N):
     arr.append(int(input()))

count=0
for i in arr:
    temp=i
    for j in arr:
        if(j>=temp):
            count+=1
    if(count==K):
        print("Special value is: ",i) 
        exit() 
    count=0      