# Divide the apples
n=int(input("Enter the number of apples does Harry potter have:"))
mn=int(input("Enter the minimum range "))
mx=int(input("Enter the maximum range"))

if mn==mx:
    print(f"There is no range between {mn} and {mx}..Enter the correct input")

else:
    for i in range(mn,mx):
       try:
        if n%i==0:
           print(f"{i} is a divisor of {n}")
        elif n%i!=0:
            print(f"{i} is not a divisor of {n}")
       except Exception as e:
           print("ZeroDivisionError,You can not divide a number by zero:",e)