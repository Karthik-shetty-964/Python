# Built in functions
# a=[2,3,7]
# c=sum(a)
# print(c)

# User-defined functions

# Fuctions with no arguements
# def handsome():
#     print("Kathik is the only handsome guy on earth")
#
# handsome()

# Fuctions with arguements and return value
# Doc_String
def fun_avg(a, b):
    """This function will calculate the average of two numbers for you"""
    avg = (a + b) / 2
    return avg


average = fun_avg(4, 2)
# print(average)
print(fun_avg.__doc__)
