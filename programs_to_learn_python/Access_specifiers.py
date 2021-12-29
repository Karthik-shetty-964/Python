class Main():
    _n=20
    __priv=239598

class Sub(Main):
    a=22

class random:
    pass

obj=Sub()
print(obj._n)

karthik=Main()
print(karthik._Main__priv)
print(obj._Main__priv)