import random

# print(comp_choice)
User=0;
Computer=0;
Draw=0;
i=0
print("\nGet ready to play the stone,paper,scissor against the beast Computer..\nMatch will be of 10 rounds..\nHighest Scorer out of 10 will be the Winner..\n")
while(i<10):
    i+=1
    list = ["s", "p", "c"]  # s-stone, p-paper , c-scissor
    comp_choice = random.choice(list)
    user_choice=input("Enter s-Stone,p-paper and c-Scissor\n")
    if comp_choice==user_choice:
        print("Both chose same..Draw!!")
        Draw+=1
    elif comp_choice=="s" and user_choice=="p":
        print("Computer chose stone you chose paper...You win!!")
        User+=1
    elif comp_choice=="s" and user_choice=="c":
        print("Computer chose stone you chose Scissor...You loose!!")
        Computer+=1
    elif comp_choice=="p" and user_choice=="s":
        print("Computer chose paper you chose stone...You loose!!")
        Computer+=1
    elif comp_choice == "p" and user_choice == "c":
        print("Computer chose paper you chose scissor...You win!!")
        User+= 1
    elif comp_choice=="c" and user_choice=="s":
        print("Computer chose scissor you chose stone...You win!!")
        User+=1
    elif comp_choice=="c" and user_choice=="p":
        print("Computer chose scissor you chose paper...You loose!!")
        Computer+=1
    else :
        print("Enter a valid choice and Play again..")

print("\n\t\t\t..GAME ENDED..\n")
print("\t----Score board----")
print("You\t\tComputer\tDraw")
print(User,"\t\t",Computer,"\t\t\t",Draw)



