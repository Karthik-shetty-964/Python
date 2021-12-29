print("Enter the  operands")
a=int(input())
b=int(input())
print("Enter '+' for addition\nEnter '-' for subtraction\nEnter '*' for multiplication\nEnter '/' for division")
op=input()
if op=="+":
    if(a==56 and b==9):
        print(77)
    else:
        print(a+b)
elif op=="-":
    print(a-b)
elif op=='*':
    if (a ==45 and b == 3):
        print(555)
    else:
        print(a*b)
elif op=='/':
    if (a ==56 and b == 6):
        print(4)
    else:
        print(a/b)
else:
    print("Enter a valid operator")