import os
fromp = input()
top = input()
with open(top, 'w') as copy_txt:
    with open(fromp) as paste_txt:
        copy_txt.write(str(paste_txt.read()))
    with open(top) as copy_txt:
        print(copy_txt.read())