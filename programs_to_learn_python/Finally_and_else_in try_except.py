f1=open("karthik.txt")

try:
    f2=open("poonki.txt")

# except Exception as e:
#     print(e)
except EOFError as e:
    print("Main huun End of file error bhai")

except IOError as e:
    print("Mai huun IO error bhai",e)

else:
    print("I only gets execute if except is not is not getting executed ")

finally:
    #finally gets excuted no matter what the
    print(" I am the finally baby//")
    f1.close()

print("This is important baby")