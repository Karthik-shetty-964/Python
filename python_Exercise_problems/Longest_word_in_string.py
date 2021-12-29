sen=input("Enter your sentence ")
list=sen.split()
print(list)
length=0
index=0
for word in list:
    wordLength=len(word)
    if wordLength>length:
        length=wordLength
        index=list.index(word)
print("The longest word in the sentence is ",list[index],"of length= ",length)