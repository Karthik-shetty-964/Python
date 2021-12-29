"""
Author:Karthik shetty
"""
# n=int(input('Enter the number of testcases'))
# flag=0
# for i in range(n):
#     number=input("Enter the number ")
#     while(True):
#         number=str(int(number)+1)
#         for i in range(len(number)//2):
#                 if number[i]==number[len(number)-1-i]:
#                      flag=1
#                 else:
#                      flag=0
#                      break
#
#         if flag==1:
#                 print(f"Next  palindrome number is {number}")
#                 break



# Another clean way to solve this:
"""
Author:Harry
"""
def next_palindrome(n):
    n+=1
    while not is_palindrome(n):
        n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__ == '__main__':
    n=int(input("Enter the number of test cases"))
    numbers=[]
    for i in range(n):
        number=int(input("Enter the number"))
        numbers.append(number)
    for i in range(n):
        print(f"The next palindrome of {numbers[i]} is {next_palindrome(numbers[i])}")

