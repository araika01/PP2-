import os
path = input()
if os.path.exists(path):
    os.remove(path)
else:
    print('File does nit exist')