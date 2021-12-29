# In which year you will become 100 years old.

def age(a):
    if int(a)<=0:
        print("You are not yet born..Please enter the correct age.")
    elif int(a)>=100:
        print("You have already crossed 100 years Legend.Live long..")
    else:
        age=2021-int(a)
        print(f"You will become 100 years old in the year {age+100}")


def years(a):
     print(f"You are 100 years old in the year {int(a)+100}")

if __name__ == '__main__':
    a=input("Enter your age or the year you were born:")
    if len(a)<=3:
        age(a)
    else:
        years(a)
    while True:
        print("Enter 1 if you wanna check your age at a particular year,\n Enter 0 to exit the portal")
        i=int(input())
        if i==1:
            print("Enter the year: ")
            j=int(input())
            print(f"Your age in {j} will be {j-int(a)}")
        elif i==0:
            exit()
        else:
            print("Enter a valid choice")
