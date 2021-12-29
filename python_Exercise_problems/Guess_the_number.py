"""
Author:Karthik shetty
Date:11th October,2021
Topic:Guess the number multiplayer game
"""
import random

def guessTheNumber():
    count=1
    while True:
        n = int(input())
        if n==rand_number:
            return count
        elif n<rand_number:
            print("Wrong!!Guess bigger number")
            count+=1
        else:
            print("Wrong!!Guess smaller number")
            count+=1

if __name__ == '__main__':
    print("Welcome to Guess the number multiplayer game!!")
    n=int(input("Enter the total number of players"))
    player=[]
    counts=[]
    for i in range(n):
        name=input(f"Enter Player{i+1}'s name: ")
        player.append(name)

    for i in range(n):
        rand_number = random.randint(1, 100)
        print("A random number between 1-100 is generated.. Try to Guess the number")
        print(f"{player[i]}'s Turn..")
        count=guessTheNumber()
        counts.append(count)
        print(f"Congrats!!You guessed it in {count} attempts.\n")

    print("\n\t\tSCORE TABLE")
    for i in range(n):
        print(f"{player[i]} --> {counts[i]} attempts")
    # index=counts.index(min(counts))
    # print(f"\n{player[index]} is the WINNER of the game")
    minimum=min(counts)
    for i in range(n):
        if(counts[i]==minimum):
            print(f"\n{player[i]} is the WINNER of the game")

    # print(rand_number)