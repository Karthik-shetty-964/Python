#Important  notes on functoions

# def func1():
#     print("Karthik is so fuking handsome")
#
# func2=func1
# del func1
# print(func2())

#we can pass built-in functions as arguements and return values
# def funreturn(n):
#     if n==0:
#         return print
#     elif n==1:
#         return int
#     else:
#         return sum
#
# print(funreturn(0))
# print(funreturn(2))
# print(funreturn(1))

#we can also assign functions to variables
# def executor(karthik):
#     karthik("This is new python were karthik is used instead of print")
#
# executor(print)



"""decorators"""

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

# def who_is_karthik():
#     print("karthik is a good boy")
#
# who_is_karthik=dec1(who_is_karthik)
# who_is_karthik()

"""This above thing can be done using decorators"""
@dec1
def who_is_karthik():
    print("karthik is a good boy")

who_is_karthik()