Dictionary={"Karthik":"A very handsome man",
            "Python ":"A programing language",
            "Cat":"It says meow",
            "Dog":"It says bow bow bow",
            "Cow":"It says mooooo moooo",
            "Birds":{"parrot":"Green","pigeon":"black"}}
# key=input()
# print(Dictionary.get(key))
Dictionary.update({"Bitch":"A girl Dog"})
print(Dictionary)
del Dictionary["Cow"]
Dictionary["vikings"]="Valhalla"
dict=Dictionary.copy()

del dict["vikings"]
# print(dict)
print(Dictionary)
print(dict.items())