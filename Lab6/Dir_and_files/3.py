import os
path = input()
if os.path.exists(path):
    for i in os.listdir(path):
        if os.path.isdir(i):
            folder = path + '\\' + i
            print(str(i) + ':')
            for i in os.listdir(folder):
                print(i, end = ' ')
        else:
            print(i)
else:
    print("Pass does not exist!")
