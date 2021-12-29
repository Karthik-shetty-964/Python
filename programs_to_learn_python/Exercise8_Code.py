# Ooooo soldier pretify my folder
import os
def soldier(directory,text_file,typeOfFile):
    # captilzing file contents
    f=open(text_file,"r+")
    content=f.read()
    var=content.split("\n")
    print(var)
    f.close()
    f=open(text_file,"w")
    for item in var:
        a=item.capitalize()
        f.write(f"{a}\n")
    f.close()

    # numbering the directories
    os.chdir(directory);
    list=os.listdir(directory)
    j=0
    for i in list:

        print(i)
        item1=i.split(".")[0]
        item2=i.split(".")[1]
        if item2 in i:
            os.rename(i,f"{j}.jpg")
            j+=1
        else:
            continue


sold=soldier("C:/Users/dell/PycharmProjects/firsrprog/Exercise8","Exercise8/text.txt",'jpg')