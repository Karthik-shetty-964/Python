"""
Author:Karthik shetty
Date:11th October,2021
Topic:Palindromifying the list
"""
def next_palindrome(n):
    n+=1
    while not is_palindrome(n):
       n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__ == '__main__':
    n=int(input("Enter the number of elements in the list"))
    numbers=[]
    Next_palindrom=[]
    for i in range(n):
        number=int(input("Enter the number"))
        numbers.append(number)
    for i in range(n):
        if numbers[i]<=10:
            Next_palindrom.append(numbers[i])
        else:
            n=next_palindrome(numbers[i])
            Next_palindrom.append(n)
    print("The next palindrome list is ",Next_palindrom)