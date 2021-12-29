import time

intial=time.time()
# print(intial)
for i in range(10):
    print("I hate everyone")
    time.sleep(2)

print(time.time()-intial)

#To get local time

# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)