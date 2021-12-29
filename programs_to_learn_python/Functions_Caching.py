import time
from functools import lru_cache

# @lru_cache #We can even specify the maximum number of calls to  be saved
@lru_cache(maxsize=4)  #maxsize is used to store the number of entries that needs to be stored
def some_work(n):
    # This function takes n seconds to execute
    time.sleep(n)
    # return n

if __name__ == '__main__':
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("Done ")
    some_work(3)
    print("Done again")
    some_work(9)
    print("Done again and again")