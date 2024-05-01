import os
folder = input()
folder1 = input()
a = r'C:\Users\Админ\Desktop'
path1 = os.path.join(a, folder)
os.mkdir(path1)
for i in  os.listdir(path1):
    if  os.path.isfile(path1 + '//' + i):
        f = open('1.txt', "r")
        f.close()
path2 = os.path.join(a, folder1)
os.mkdir(path2)
for g in os.listdir(path1):
    os.replace(path1 + g, path2 + g)