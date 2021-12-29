print("Enter the  rows")
n=int(input())
print("Enter 0-False and 1-True")
con=int(input())
if con==1:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()
if con==0:
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")
        print()

