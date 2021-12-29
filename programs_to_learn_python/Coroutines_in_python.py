# def searcher():
#     import time
#     # Assume loading this book takes 4 seconds
#     book="This is the biggest book and it has so many pages that it takes few minutes to load it"
#     time.sleep(4)
#
#     while True:
#         item=(yield)
#         if item in book:
#             print("Your word is present in the book")
#         else:
#             print("Word is not present in the book")
#
# search=searcher()
# print("search started")
# next(search)
# search.send("book")
# search.send("takes")
# search.close()
# # search2=searcher()
# # next(search2)
# # search2.send("load")


# practise problem
def finder():
    import time
    # Assune that we are loading dictionary
    name_dict=["karthik","shreya","kishan","apeksha","jithin","muneez","keerthan","jnanesh"]
    time.sleep(4)

    while True:
        name=(yield )
        if name in name_dict:
            print(f"Name \"{name}\"is present in the name dictionary")
        else:
            print(f"Name \"{name}\"is not present in the name dictionary")

find=finder()
find.__next__ ()
find.send("karthik")
find.send("shreya")
find.send("muneez")
find.send("peddanna")
find.close()