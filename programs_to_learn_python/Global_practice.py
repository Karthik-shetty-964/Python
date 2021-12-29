l=40

def function():
    # l=3
    #we cannot modify the global variable inside the function
    global l
    l= l+5
    print(l)
function()
print(l)